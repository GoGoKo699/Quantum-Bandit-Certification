#!/usr/bin/env python3
"""Finite checks of the reward-halfspace certification constructions.

Run from any directory. Results are written beside this script. These checks
exercise numerical identities and boundary constructions; they do not prove
the all-block optimization or asymptotic certification theorem.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad_vec
from scipy.optimize import brentq, minimize, minimize_scalar
from scipy.stats import binom


SEED = 20261115
RNG = np.random.default_rng(SEED)
IDENTITY_TOL = 3e-9
ENTROPY_TOL = 2e-8


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def kl(p: np.ndarray, q: np.ndarray) -> float:
    active = p > 0
    if np.any(q[active] <= 0):
        return math.inf
    return float(np.dot(p[active], np.log(p[active] / q[active])))


def binary_kl(p: float, q: float) -> float:
    return kl(np.array([p, 1 - p]), np.array([q, 1 - q]))


def classical_dual(p: np.ndarray, f: np.ndarray, r: float) -> tuple[float, np.ndarray, float]:
    """Scalar reverse-KL dual, including endpoint leakage into an absent top atom."""
    active = p > 0
    upper = 1.0 / (float(np.max(f)) - r)

    def derivative(lam: float) -> float:
        w = 1 - lam * (f[active] - r)
        if np.any(w <= 0):
            return -math.inf
        return float(-np.dot(p[active], (f[active] - r) / w))

    endpoint_w = 1 - upper * (f[active] - r)
    if np.all(endpoint_w > 1e-13) and derivative(upper) >= 0:
        lam = upper
    else:
        lam = brentq(derivative, 0, upper * (1 - 1e-13), xtol=1e-14)
    omega = 1 - lam * (f - r)
    q = np.zeros_like(p)
    q[active] = p[active] / omega[active]
    leftover = 1 - float(np.sum(q))
    if leftover > 1e-10:
        top = int(np.argmax(f))
        require(not active[top], "Dual leakage entered an active top atom")
        q[top] = leftover
    require(abs(float(np.sum(q)) - 1) < 2e-9, "Dual optimizer is not normalized")
    require(abs(float(np.dot(q, f)) - r) < 2e-9, "Dual mean constraint does not bind")
    return kl(p, q), q, lam


def classical_primal(p: np.ndarray, f: np.ndarray, r: float) -> tuple[float, np.ndarray]:
    """Independent optimization over all simplex coordinates using SLSQP."""
    length = len(p)
    uniform = np.full(length, 1 / length)
    top = np.zeros(length)
    top[int(np.argmax(f))] = 1
    mix = max(0.0, (r - float(f @ uniform)) / (float(np.max(f)) - float(f @ uniform)))
    q0 = (1 - (mix + 1) / 2) * uniform + (mix + 1) / 2 * top
    active = p > 0

    def objective(q: np.ndarray) -> float:
        return kl(p, q)

    def gradient(q: np.ndarray) -> np.ndarray:
        result = np.zeros_like(q)
        result[active] = -p[active] / q[active]
        return result

    result = minimize(
        objective,
        q0,
        jac=gradient,
        method="SLSQP",
        bounds=[(1e-12 if positive else 0.0, 1.0) for positive in active],
        constraints=[
            {"type": "eq", "fun": lambda q: float(np.sum(q) - 1), "jac": lambda q: np.ones(length)},
            {"type": "ineq", "fun": lambda q: float(f @ q - r), "jac": lambda q: f},
        ],
        options={"ftol": 2e-13, "maxiter": 2000},
    )
    require(bool(result.success), f"Primal optimization failed: {result.message}")
    require(abs(float(np.sum(result.x)) - 1) < 1e-8, "Primal optimizer not normalized")
    require(float(f @ result.x) >= r - 1e-8, "Primal optimizer not feasible")
    return float(result.fun), result.x


def tensor_power(matrix: np.ndarray, n: int) -> np.ndarray:
    out = np.array([[1.0 + 0j]])
    for _ in range(n):
        out = np.kron(out, matrix)
    return out


def tensor_sums(values: np.ndarray, n: int) -> np.ndarray:
    out = np.array([0.0])
    for _ in range(n):
        out = (out[:, None] + values[None, :]).reshape(-1)
    return out


def groups(values: np.ndarray, tol: float = 2e-10) -> tuple[np.ndarray, int]:
    labels = np.empty(len(values), dtype=int)
    representative: list[float] = []
    for index in np.argsort(values):
        value = float(values[index])
        if not representative or abs(value - representative[-1]) > tol:
            representative.append(value)
        labels[index] = len(representative) - 1
    return labels, len(representative)


def pinching(matrix: np.ndarray, log_eigenvalues: np.ndarray) -> tuple[np.ndarray, int]:
    labels, count = groups(log_eigenvalues)
    return matrix * (labels[:, None] == labels[None, :]), count


def log_derivative_loewner(a: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Direct divided differences, independent of the modular integral."""
    values, vectors = np.linalg.eigh(a)
    require(float(values.min()) > 0, "Loewner derivative called outside positive support")
    xx = vectors.conj().T @ x @ vectors
    multipliers = np.empty((len(values), len(values)))
    for j, left in enumerate(values):
        for k, right in enumerate(values):
            if abs(left - right) < 1e-11 * max(left, right):
                multipliers[j, k] = 1 / ((left + right) / 2)
            else:
                multipliers[j, k] = (math.log(left) - math.log(right)) / (left - right)
    return vectors @ (multipliers * xx) @ vectors.conj().T


def entropy(rho: np.ndarray) -> float:
    values = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    require(float(values.min()) > -2e-10, "Entropy input is not positive")
    values = values[values > 1e-12]
    return float(-np.dot(values, np.log(values)))


def relative_entropy(rho: np.ndarray, sigma: np.ndarray) -> float:
    values, vectors = np.linalg.eigh((sigma + sigma.conj().T) / 2)
    require(float(values.min()) > -2e-10, "Relative-entropy alternative not positive")
    positive = values > 1e-12
    if np.any(~positive):
        missing = vectors[:, ~positive]
        unsupported = float(np.trace(missing.conj().T @ rho @ missing).real)
        require(unsupported < 2e-9, "Relative-entropy support inclusion failed")
    log_sigma = (vectors[:, positive] * np.log(values[positive])) @ vectors[:, positive].conj().T
    return -entropy(rho) - float(np.trace(rho @ log_sigma).real)


def random_unitary(d: int) -> np.ndarray:
    z = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
    q, rr = np.linalg.qr(z)
    return q @ np.diag(np.exp(-1j * np.angle(np.diag(rr))))


def random_state(d: int) -> np.ndarray:
    z = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
    raw = z @ z.conj().T
    return 0.6 * raw / np.trace(raw) + 0.4 * np.eye(d) / d


@dataclass
class Case:
    name: str
    rho: np.ndarray  # Written in an F eigenbasis; arbitrary world bases are tested too.
    f: np.ndarray  # Distinct reward eigenvalues.
    atoms: np.ndarray  # Spectral atom index of each basis vector.
    r: float
    ns: tuple[int, ...]

    def populations(self) -> np.ndarray:
        return np.array([np.trace(self.rho[np.ix_(self.atoms == i, self.atoms == i)]).real for i in range(len(self.f))])


def build_cases() -> list[Case]:
    coherent = np.array([[0.5, 0.45], [0.45, 0.5]], complex)
    pure = np.full((2, 2), 0.5, complex)
    absent = np.array([[0.6, 0.2 + 0.1j, 0], [0.2 - 0.1j, 0.4, 0], [0, 0, 0]], complex)
    full3 = random_state(3)
    f3 = np.array([0.0, 0.35, 1.0])
    mean3 = float(np.dot(np.diag(full3).real, f3))
    degenerate = random_state(4)
    atom4 = np.array([0, 0, 1, 1])
    mean4 = float(np.trace(degenerate[2:, 2:]).real)
    return [
        Case("coherent_qubit", coherent, np.array([1.0, 0.0]), np.array([0, 1]), 0.95, (1, 2, 3, 4)),
        Case("pure_qubit", pure, np.array([1.0, 0.0]), np.array([0, 1]), 0.85, (1, 2, 3, 4)),
        Case("zero_population_leakage", absent, np.array([0.0, 0.5, 1.0]), np.array([0, 1, 2]), 0.8, (1, 2, 3)),
        Case("full_rank_three_atom", full3, f3, np.arange(3), mean3 + 0.55 * (1 - mean3), (1, 2, 3)),
        Case("degenerate_projector", degenerate, np.array([0.0, 1.0]), atom4, mean4 + 0.6 * (1 - mean4), (1, 2)),
        Case("pure_reward_eigenstate", np.diag([1.0, 0.0]).astype(complex), np.array([0.0, 1.0]), np.arange(2), 0.7, (1, 2, 3, 4)),
    ]


def orbit_data(case: Case) -> dict:
    p = case.populations()
    k, q, lam = classical_dual(p, case.f, case.r)
    active_atoms = p > 1e-14
    active_indices = np.flatnonzero(active_atoms[case.atoms])
    active_p = p[active_atoms]
    active_q = q[active_atoms]
    omega_atom = np.zeros_like(p)
    omega_atom[active_atoms] = active_p / active_q
    w = omega_atom[case.atoms[active_indices]]
    rho_s = case.rho[np.ix_(active_indices, active_indices)]
    chi_s = rho_s / np.sqrt(w[:, None] * w[None, :])
    base = np.zeros_like(case.rho)
    base[np.ix_(active_indices, active_indices)] = chi_s
    for atom in np.flatnonzero(~active_atoms):
        indices = np.flatnonzero(case.atoms == atom)
        base[indices, indices] = q[atom] / len(indices)
    h = np.zeros(len(case.rho))
    h[active_indices] = np.log(w) / 2

    def sigma(t: float) -> np.ndarray:
        phases = np.exp(-1j * t * h)
        return phases[:, None] * base * phases.conj()[None, :]

    for t in (0.0, 0.7, -3.1):
        st = sigma(t)
        require(abs(float(np.trace(st).real) - 1) < 2e-10, "Orbit is not normalized")
        require(float(np.linalg.eigvalsh(st).min()) > -2e-10, "Orbit is not positive")
        got = np.array([np.trace(st[np.ix_(case.atoms == i, case.atoms == i)]).real for i in range(len(case.f))])
        require(float(np.max(np.abs(got - q))) < 2e-10, "Orbit has incorrect populations")
        require(float(got @ case.f) >= case.r - 2e-10, "Orbit leaves alternative halfspace")
    return dict(p=p, q=q, K=k, lam=lam, active_indices=active_indices, w=w, rho_s=rho_s, base=base, h=h, sigma=sigma)


def null_tensor_indices(active_indices: np.ndarray, d: int, n: int) -> np.ndarray:
    return np.array([sum(index * d ** (n - j - 1) for j, index in enumerate(word)) for word in itertools.product(active_indices, repeat=n)])


def exact_tail(p: np.ndarray, z: np.ndarray, n: int, c: float) -> float:
    total = 0.0
    cutoff = n * c
    tolerance = 2e-12 * max(1, abs(cutoff))
    for word in itertools.product(range(len(p)), repeat=n):
        if sum(z[index] for index in word) > cutoff + tolerance:
            total += math.prod(float(p[index]) for index in word)
    return total


def check_classical() -> dict:
    triples: list[tuple[np.ndarray, np.ndarray, float]] = [
        (np.array([0.6, 0.4, 0.0]), np.array([0.0, 0.5, 1.0]), 0.8),
        (np.array([0.5, 0.5]), np.array([0.0, 1.0]), 0.95),
    ]
    for length in range(2, 6):
        for trial in range(4):
            p = RNG.dirichlet(np.ones(length))
            if trial == 0 and length > 2:
                p[-1] = 0
                p /= p.sum()
            f = np.sort(RNG.uniform(0.02, 0.98, length))
            mean = float(p @ f)
            r = mean + RNG.uniform(0.2, 0.8) * (float(f.max()) - mean)
            triples.append((p, f, r))
    max_value_error = 0.0
    max_witness_excess = 0.0
    leakage_error = 0.0
    for j, (p, f, r) in enumerate(triples):
        kd, qd, lam = classical_dual(p, f, r)
        kp, qp = classical_primal(p, f, r)
        error = abs(kd - kp)
        require(error < 3e-7, f"Primal/dual value mismatch in classical case {j}: {error}")
        max_value_error = max(max_value_error, error)
        omega = np.zeros_like(p)
        omega[p > 0] = p[p > 0] / qd[p > 0]
        for _ in range(12):
            candidate = RNG.dirichlet(np.ones(len(p)))
            if float(candidate @ f) < r:
                top = np.zeros(len(p))
                top[int(np.argmax(f))] = 1
                fraction = (r - float(candidate @ f)) / (float(f.max()) - float(candidate @ f))
                candidate = (1 - fraction) * candidate + fraction * top
            excess = float(omega @ candidate) - 1
            require(excess < 2e-8, "Classical first-order mixture witness has wrong sign")
            max_witness_excess = max(max_witness_excess, max(0.0, excess))
        if j == 0:
            expected = np.array([0.12, 0.16, 0.72])
            leakage_error = float(max(np.max(np.abs(qd - expected)), np.max(np.abs(qp - expected))))
            require(leakage_error < 2e-6, "Claimed zero-population optimizer is not optimal")
    binary_error = 0.0
    for p1, r in [(0.0, 0.7), (0.13, 0.45), (0.5, 0.95), (0.76, 0.9)]:
        k, _, _ = classical_dual(np.array([1 - p1, p1]), np.array([0.0, 1.0]), r)
        binary_error = max(binary_error, abs(k - binary_kl(p1, r)))
    require(binary_error < 2e-10, "Binary dual disagrees with its closed value")
    return dict(cases=len(triples), max_primal_dual_value_error=max_value_error, zero_population_q_error=leakage_error, max_first_order_witness_excess=max_witness_excess, max_binary_closed_value_error=binary_error)


def check_constructions(cases: list[Case]) -> dict:
    records = []
    max_quad_error = 0.0
    max_phase_error = 0.0
    max_entropy_error = 0.0
    max_converse_violation = 0.0
    finite_effects = 0
    nonzero_lower_bounds = 0
    independent_average_separation = 0.0
    for case in cases:
        data = orbit_data(case)
        d = len(case.rho)
        active = data["active_indices"]
        w = data["w"]
        rho_s = data["rho_s"]
        sigma = data["sigma"]
        world_basis = random_unitary(d)
        max_case_error = 0.0
        for n in case.ns:
            full_rho = tensor_power(case.rho, n)
            r_n = tensor_power(rho_s, n)
            log_w = tensor_sums(np.log(w), n)
            w_n = np.diag(np.exp(log_w))
            derivative = log_derivative_loewner(w_n, r_n)
            full_indices = null_tensor_indices(active, d, n)
            world_n = tensor_power(world_basis, n)

            # Integrate complete physical tensor states with one shared t.
            def integrand(t: float) -> np.ndarray:
                beta = math.pi / (2 * (math.cosh(math.pi * t) + 1))
                return beta * tensor_power(sigma(t), n)

            quadrature, quadrature_error = quad_vec(integrand, -12.0, 12.0, epsabs=2e-10, epsrel=2e-10)
            require(float(quadrature_error) < 2e-8, "Modular quadrature did not converge")
            require(abs(float(np.trace(quadrature).real) - 1) < IDENTITY_TOL, "Quadrature mixture not normalized")
            qblock = quadrature[np.ix_(full_indices, full_indices)]
            error = float(np.max(np.abs(qblock - derivative)))
            require(error < IDENTITY_TOL, f"Modular integral/Loewner mismatch: {case.name}, n={n}")
            max_case_error = max(max_case_error, error)
            max_quad_error = max(max_quad_error, error)
            # Test covariance in a non-reward-diagonal physical basis as well.
            transformed = world_n @ quadrature @ world_n.conj().T
            support_embedding = world_n[:, full_indices]
            require(float(np.max(np.abs(support_embedding.conj().T @ transformed @ support_embedding - derivative))) < IDENTITY_TOL, "Rotated-support comparison failed")
            variational_value = float(np.trace(r_n @ np.diag(log_w)).real + 1 - np.trace(qblock @ w_n).real)
            require(abs(variational_value - n * data["K"]) < IDENTITY_TOL, "Measured-divergence witness objective mismatch")

            # Cesaro limit is an independent pinching of the full unnormalized-sector construction.
            full_h_n = tensor_sums(data["h"], n)
            eta, _ = pinching(tensor_power(data["base"], n), full_h_n)
            require(abs(float(np.trace(eta).real) - 1) < IDENTITY_TOL, "Cesaro witness not normalized")
            e_r, v = pinching(r_n, log_w)
            predicted_block = e_r / np.sqrt(np.exp(log_w[:, None] + log_w[None, :]))
            require(float(np.max(np.abs(eta[np.ix_(full_indices, full_indices)] - predicted_block))) < IDENTITY_TOL, "Cesaro null-support block lost its leakage factor")
            distinct_single = groups(np.log(w))[1]
            require(v <= math.comb(n + distinct_single - 1, distinct_single - 1), "Pinching count exceeds the type bound")
            require(float(np.linalg.eigvalsh(v * e_r - r_n).min()) > -IDENTITY_TOL, "Pinching inequality has the wrong direction")

            # In every two-frequency case, an exact discrete periodic average is available.
            unique_log = np.unique(np.round(np.log(w), 12))
            if len(unique_log) <= 2:
                if len(unique_log) == 1:
                    periodic_average = tensor_power(sigma(0), n)
                else:
                    period = 4 * math.pi / abs(float(unique_log[1] - unique_log[0]))
                    points = 2 * n + 3
                    periodic_average = sum(tensor_power(sigma(period * j / points), n) for j in range(points)) / points
                phase_error = float(np.max(np.abs(periodic_average - eta)))
                require(phase_error < IDENTITY_TOL, "Periodic physical orbit average disagrees with pinching")
                max_phase_error = max(max_phase_error, phase_error)

            coherence = relative_entropy(r_n, e_r)
            direct_entropy = relative_entropy(full_rho, eta)
            entropy_error = abs(direct_entropy - n * data["K"] - coherence)
            require(entropy_error < ENTROPY_TOL, "Relative-entropy mixture identity failed")
            require(coherence >= -ENTROPY_TOL and coherence <= math.log(v) + ENTROPY_TOL, "Coherence/pinching entropy bound failed")
            require(abs(coherence - (entropy(e_r) - entropy(r_n))) < ENTROPY_TOL, "Coherence entropy independently disagrees")
            max_entropy_error = max(max_entropy_error, entropy_error)

            active_atoms = data["p"] > 0
            p_active = data["p"][active_atoms]
            z = np.log(data["p"][active_atoms] / data["q"][active_atoms])
            cs = [data["K"] - 0.1, data["K"], data["K"] + 0.2, float(np.max(z))]
            for trial in range(7):
                if trial == 0:
                    effect = np.eye(d**n, dtype=complex)
                else:
                    basis = random_unitary(d**n)
                    values = RNG.uniform(0, 1, d**n)
                    values[0] = 0
                    values[-1] = 1
                    effect = (basis * values) @ basis.conj().T
                acceptance = float(np.trace(full_rho @ effect).real)
                mixture_acceptance = float(np.trace(eta @ effect).real)
                for c in cs:
                    tail = exact_tail(p_active, z, n, c)
                    lower = math.exp(-n * c) * max(0.0, acceptance / v - tail)
                    violation = lower - mixture_acceptance
                    require(violation < IDENTITY_TOL, "Exact finite-confidence converse failed")
                    max_converse_violation = max(max_converse_violation, max(0.0, violation))
                    nonzero_lower_bounds += int(lower > 1e-12)
                    finite_effects += 1
            if case.name == "coherent_qubit" and n == 2:
                one, _ = quad_vec(lambda t: math.pi / (2 * (math.cosh(math.pi * t) + 1)) * sigma(t), -12, 12, epsabs=2e-11)
                independent_average_separation = float(np.max(np.abs(quadrature - np.kron(one, one))))
                require(independent_average_separation > 1e-3, "Test does not distinguish shared and independent modular phases")
        records.append(dict(name=case.name, dimension=d, copy_counts=list(case.ns), populations=data["p"].tolist(), optimizer=data["q"].tolist(), K_nats=data["K"], max_modular_identity_error=max_case_error))
    require(nonzero_lower_bounds > finite_effects // 5, "Converse checks are mostly vacuous zero bounds")
    return dict(cases=records, max_modular_quadrature_error=max_quad_error, max_periodic_average_error=max_phase_error, max_relative_entropy_identity_error=max_entropy_error, finite_confidence_effect_threshold_checks=finite_effects, positive_finite_confidence_bounds=nonzero_lower_bounds, max_finite_confidence_violation=max_converse_violation, shared_vs_independent_phase_matrix_separation=independent_average_separation)


def check_qubit_example() -> dict:
    p, r, s, n = 0.5, 0.95, 0.8, 33
    cutoff = math.floor(n * s)
    exact_alpha = float(binom.sf(cutoff, n, p))
    exact_beta = float(binom.cdf(cutoff, n, r))
    chernoff_alpha = math.exp(-n * binary_kl(s, p))
    chernoff_beta = math.exp(-n * binary_kl(s, r))
    require(exact_alpha <= chernoff_alpha < 0.01, "33-copy null-error guarantee failed")
    require(exact_beta <= chernoff_beta < 0.01, "33-copy worst-alternative guarantee failed")
    for alternative in np.linspace(r, 1, 21):
        require(float(binom.cdf(cutoff, n, alternative)) <= exact_beta + 1e-14, "Binomial alternative maximum not at the threshold")
    rho = np.array([[0.5, 0.45], [0.45, 0.5]])
    k = 0.5 * math.log(100 / 19)

    # Numerical reconstruction of the inherited pointwise comparator, not a certified optimum.
    def pointwise(c: float) -> float:
        return relative_entropy(rho, np.array([[r, c], [c, 1 - r]]))

    cap = math.sqrt(r * (1 - r))
    comparison = minimize_scalar(pointwise, bounds=(-cap + 1e-9, cap - 1e-9), method="bounded", options={"xatol": 1e-12})
    require(bool(comparison.success), "Pointwise numerical comparison did not converge")
    require(abs(float(comparison.fun) - 1.11733005476175) < 2e-7, "Inherited qubit numerical comparator not reproduced")
    return dict(copies=n, accept_at_most_successes=cutoff, exact_type_I=exact_alpha, exact_worst_type_II=exact_beta, chernoff_type_I=chernoff_alpha, chernoff_worst_type_II=chernoff_beta, K_nats=k, pointwise_Umegaki_reconstruction=float(comparison.fun), pointwise_alternative_coherence=float(comparison.x), pointwise_comparison_scope="one-dimensional real-coherence numerical minimization; not a certified global optimization")


def main() -> None:
    classical = check_classical()
    constructions = check_constructions(build_cases())
    example = check_qubit_example()
    script = Path(__file__).resolve()
    results = {
        "status": "passed",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "seed": SEED,
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "tolerances": {"matrix_identity_absolute": IDENTITY_TOL, "relative_entropy_absolute": ENTROPY_TOL},
        "classical_optimization": classical,
        "quantum_constructions": constructions,
        "qubit_example": example,
        "limits": [
            "Floating-point finite-dimensional checks, not interval arithmetic or a proof certificate.",
            "No optimization over all collective POVMs or all alternative states is performed.",
            "Finite checks do not establish asymptotic exponents, the all-block game theorem, or novelty.",
            "No arbitrary-memory adaptive bandit regret, gate synthesis, hardware noise, or runtime advantage is verified.",
        ],
    }
    destination = script.with_name("results.json")
    destination.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"status": "passed", "classical_cases": classical["cases"], "quantum_cases": len(constructions["cases"]), "effect_threshold_checks": constructions["finite_confidence_effect_threshold_checks"], "max_modular_error": constructions["max_modular_quadrature_error"], "max_entropy_error": constructions["max_relative_entropy_identity_error"], "results": str(destination)}, indent=2))


if __name__ == "__main__":
    main()

"""Rational bounds for the two-arm adaptive-regret example."""

from fractions import Fraction


def log_ratio_bounds(ratio: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Enclose log(ratio) for a rational ratio at least one."""
    step = (ratio - 1) / (ratio + 1)
    lower = 2 * sum(step ** (2 * k + 1) / (2 * k + 1) for k in range(terms))
    tail = 2 * step ** (2 * terms + 1) / ((2 * terms + 1) * (1 - step**2))
    return lower, lower + tail


def check_adaptive_qubit_example() -> dict:
    x = Fraction(7, 25)
    z = Fraction(9, 10)
    radius_squared = x**2 + z**2
    terms = 128

    # A = atanh(sqrt(radius_squared)) / sqrt(radius_squared).
    a_lower = sum(radius_squared**k / (2 * k + 1) for k in range(terms))
    a_tail = radius_squared**terms / ((2 * terms + 1) * (1 - radius_squared))
    a_upper = a_lower + a_tail

    # B = -log(1 - radius_squared).
    b_lower = sum(radius_squared**k / k for k in range(1, terms + 1))
    b_tail = radius_squared ** (terms + 1) / ((terms + 1) * (1 - radius_squared))
    b_upper = b_lower + b_tail

    log_two_lower, log_two_upper = log_ratio_bounds(Fraction(2), terms)
    value_lower = log_two_lower + b_lower / 2 - x * a_upper
    value_upper = log_two_upper + b_upper / 2 - x * a_lower
    slope_term = (x - x**2 / radius_squared) / (1 - radius_squared)
    slope_lower = slope_term - z**2 * a_upper / radius_squared
    slope_upper = slope_term - z**2 * a_lower / radius_squared
    if not Fraction(1266602, 10**6) < value_lower <= value_upper < Fraction(1266604, 10**6):
        raise RuntimeError("The displayed objective enclosure did not hold")
    if not Fraction(15306, 10**6) < slope_lower <= slope_upper < Fraction(15308, 10**6):
        raise RuntimeError("The displayed tangent slope enclosure did not hold")

    # The positive-slope tangent is smallest at zero over all feasible x'.
    quantum_lower = Fraction(631, 500)
    quantum_upper = Fraction(1267, 1000)
    if slope_lower <= 0 or value_lower - x * slope_upper <= quantum_lower:
        raise RuntimeError("The convex tangent did not certify the Umegaki lower bound")
    if value_upper >= quantum_upper:
        raise RuntimeError("The trial state did not certify the Umegaki upper bound")

    log_ratio_lower, log_ratio_upper = log_ratio_bounds(Fraction(100, 19), terms)
    classical_lower, classical_upper = log_ratio_lower / 2, log_ratio_upper / 2
    if not Fraction(830365, 1000000) < classical_lower <= classical_upper < Fraction(830366, 1000000):
        raise RuntimeError("The spectral KL enclosure failed")
    if classical_upper >= quantum_lower:
        raise RuntimeError("The strict gap between the two divergences was not certified")

    gap = Fraction(9, 20)
    return {
        "spectral_K_nats_open_interval": [0.830365, 0.830366],
        "Umegaki_D_nats_open_interval": [float(quantum_lower), float(quantum_upper)],
        "optimal_regret_coefficient_interval": [
            float(gap / Fraction(830366, 1000000)),
            float(gap / Fraction(830365, 1000000)),
        ],
        "earlier_Umegaki_lower_coefficient_interval": [
            float(gap / quantum_upper),
            float(gap / quantum_lower),
        ],
    }


def check_stopped_two_arm_example() -> dict:
    """Reduce a stopped three-round protocol with a joint SWAP readout."""
    half = Fraction(1, 2)
    first_arm = ((Fraction(3, 5), Fraction(1, 10)), (Fraction(1, 10), Fraction(2, 5)))
    second_arm = ((Fraction(2, 3), Fraction(1, 6)), (Fraction(1, 6), Fraction(1, 3)))
    symmetric_effect = (
        (1, 0, 0, 0),
        (0, half, half, 0),
        (0, half, half, 0),
        (0, 0, 0, 1),
    )
    # Pull arm 1, then arm 2. Pull arm 2 again iff the two-copy SWAP sign is +1.
    # The capped event is the +1 outcome, before the third copy is delivered.
    joint_probability = sum(
        symmetric_effect[row][column] * first_arm[column // 2][row // 2]
        * second_arm[column % 2][row % 2]
        for row in range(4)
        for column in range(4)
    )
    reduced_effect = tuple(
        tuple(half * (int(row == column) + second_arm[row][column]) for column in range(2))
        for row in range(2)
    )
    reduced_probability = sum(
        reduced_effect[row][column] * first_arm[column][row]
        for row in range(2)
        for column in range(2)
    )
    if joint_probability != reduced_probability or reduced_probability != Fraction(47, 60):
        raise RuntimeError("The reduced stopped effect did not reproduce the joint branch")
    return {"horizon": 3, "first_arm_cap": 1, "event_probability_exact": str(reduced_probability)}


if __name__ == "__main__":
    print(check_adaptive_qubit_example())
    print(check_stopped_two_arm_example())

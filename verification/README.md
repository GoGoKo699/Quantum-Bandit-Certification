# Reproduce the finite scientific checks

With Python 3.11 or later, install the pinned numerical dependencies and run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_science.py
```

The script uses a fixed random seed and writes [results.json](results.json), including its own SHA-256 hash, actual package versions, numerical errors, and the precise scope of the checks. Assertions stop execution when a claimed identity or inequality fails; a failed run does not overwrite the preceding successful result file.

## What is checked

| Scientific issue | Finite check |
| --- | --- |
| Is the classical reverse-KL optimizer correct? | Independent constrained optimization over the probability simplex is compared with the scalar dual, including the exact binary value and the missing-top-population example. The first-order mixture-witness inequality is tested on feasible distributions. |
| Is the modular phase shared across copies? | Direct quadrature of physical tensor-power states is compared with an independent Loewner divided-difference logarithm derivative. A two-copy coherent example explicitly distinguishes this shared-phase mixture from the product of single-copy averages. |
| Does the construction survive null-support boundaries? | Full-rank and pure nulls, a zero-population three-level source with optimizer $`(0.12,0.16,0.72)`$, a pure reward eigenstate, and a degenerate projector are included. Orbit positivity, trace, reward populations, leakage, and rotated support embeddings are checked. |
| Does Cesaro averaging give the stated pinching witness? | For two active modular frequencies, a discrete full-period average of actual tensor states is compared directly with pinching. The null-support block retains its unnormalized mass. |
| Is the relative-entropy remainder the pinching coherence? | Direct relative entropy to the feasible mixture is compared with $`nK+D(R_n\Vert \mathcal E_n(R_n))`$. The latter term is independently compared with the entropy increase and checked against $`\log v_n`$. |
| Does the finite-confidence converse have the correct factors and inequality direction? | IID upper-tail probabilities are enumerated exactly for the tested small copy counts. The resulting lower bound is compared with actual mixture acceptance for random noncommuting effects and the identity effect. Positive lower bounds are required so the check cannot pass only through a vacuous positive part. |
| Does the worked finite-copy test meet its promised risks? | Exact binomial tails for the 33-copy test are compared with both Chernoff bounds; the alternative maximum is checked at the threshold. |

The quantum cases use one through four copies where the dimensions remain small. The qubit example's reported pointwise Umegaki comparator is also reconstructed by a scalar numerical minimization over real coherence. That reconstruction is not a certified global optimization and is not needed by the certification proof.

## What the checks do not establish

These are floating-point diagnostics of selected finite cases. They are not interval-certified arithmetic, optimization over all POVMs, exhaustive alternative-state searches, universal proof verification, or a priority certificate. The written arguments in the scientific account establish the asymptotic certification rate and the finite-block max–min result. The suite does not establish a hardware implementation, robustness to a fixed physical noise rate, a runtime advantage, or an optimal regret coefficient for arbitrary adaptive quantum-memory policies.

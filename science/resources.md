# Inputs, measurements, and physical costs

The result concerns certification of one **known null state** against an unknown fixed IID alternative whose reward is above a threshold. It determines a statistical limit for that experiment. The model and error conventions are in [model.md](model.md); the unrestricted converse is in [certification.md](certification.md).

## What the tester receives

The tester has classical specifications of the finite-dimensional state $`\rho`$, the effect $`F`$, and the threshold $`r`$. It receives $`n`$ independent specimens from either $`\rho`$ or one fixed unknown state $`\sigma`$ satisfying $`\mathrm{Tr}(\sigma F)\ge r`$. The alternative can be chosen adversarially for the experiment, but the specimens conditional on that choice are IID. The theorem does not assume arbitrary correlated replacement sources.

Knowing $`\rho`$ is substantive input. Estimating an unknown arm state, choosing a good arm, or propagating uncertainty in a learned null is a separate task. A dense classical description of $`\rho`$ or $`F`$ can itself require order $`d^2`$ numbers when the Hilbert-space dimension is $`d`$. The certification theorem supplies no efficient tomography procedure or compact representation for an arbitrary such description.

The mixture of IID alternatives in [modular_mixtures.md](modular_mixtures.md) is a converse witness. It is a prior over a fixed source choice, shared across the entire block. It does not grant the tester access to its hidden phase parameter or describe a source that changes that parameter independently on every specimen.

## An attaining acquisition scheme

Write the known effect as

```math
F=\sum_{i=1}^{L} f_iP_i,
\qquad p_i=\mathrm{Tr}(\rho P_i).
```

Measure the spectral PVM $`\{P_i\}_{i=1}^{L}`$ on every specimen and retain its outcome. A classical empirical-distribution test then attains the exponent $`K`$. The [worked example](examples.md) gives a finite-confidence binary test; the general asymptotic construction is in [certification.md](certification.md).

For an effect with more than two eigenvalues, this is more informative than recording only a Bernoulli outcome from the two-effect measurement $`\{F,I-F\}`$. Randomizing spectral outcome $`i`$ to a Bernoulli variable with success probability $`f_i`$ preserves the reward mean but can discard the information needed to attain $`K`$. The distinction disappears for projector rewards, whose spectral statistics are already binary. This spectral-statistics distinction and the one-copy optimum are established by [Ng, §§II–III](https://arxiv.org/html/2609.40339v1).

The attaining scheme processes specimens sequentially. It needs one $`d`$-dimensional input register at a time, together with the apparatus for its PVM; it does not retain coherent memory between specimens. A straightforward implementation stores $`L`$ outcome counts using $`O(L\log(n+1))`$ classical bits, in addition to the input descriptions and numerical workspace. For a binary reward, one count suffices. The final output is one classical bit: accept or reject the null.

## Charged resources

| Resource | What is counted or supplied |
| --- | --- |
| Specimens | Every test uses $`n`$ actual supplied copies. There is no reuse of a measured specimen. |
| Data access | Direct specimen access is supplied. No QRAM, coherent state-preparation oracle, controlled unknown preparation, or inverse preparation is required. |
| Classical input | The descriptions of $`\rho`$, $`F`$, and $`r`$ are supplied; their size and processing cost are separate from copy complexity. |
| Acquiring the source | Preparing and delivering those specimens is a physical cost. The supplied-copy model does not bound source latency, preparation gates, or preparation energy. |
| Readout | The attaining protocol performs one spectral measurement of $`F`$ per copy. Its circuit cost depends on the actual implementation of $`F`$. |
| Storage | Sequential spectral readout needs one incoming quantum register and classical counts. A competing collective test may retain all $`n`$ registers and ancillary memory; its storage and coherence costs are additional resources. |
| Classical decision | Counts, numerical precision, and threshold or type-set processing must be implemented. The asymptotic theorem does not assert uniform numerical conditioning near a boundary. |
| Output | One binary certification decision is returned. No state description, reusable learned model, or list of optimal arms is produced. |

A generic dense effect is not automatically cheap to measure. Given a diagonalizing unitary $`U_F`$, one implementation applies $`U_F`$ and measures in a computational basis, grouping outcomes belonging to the same eigenspace. Constructing and compiling $`U_F`$ is a separate problem; for an arbitrary effect on $`m=\lceil\log_2d\rceil`$ qubits its cost need not be polynomial in $`m`$. A structured local effect may admit much cheaper readout. The statistical conclusion does not choose between those implementations or supply a hardware crossover.

No postselected successful branch is used by the attaining test. All specimens and all outcomes contribute to the decision. Source preparation, readout duration, classical processing, reset, and storage determine elapsed time and energy; equality of error exponents alone is not a bound on either.

## Finite precision and interpretation

The proofs use ideal source states and measurements. If the implemented single-copy measurement channel is within total variation error $`\varepsilon_{\rm meas}`$ uniformly on all input states, a hybrid argument bounds the change in either error probability after $`n`$ independent readouts by $`n\varepsilon_{\rm meas}`$. This additive bound does not preserve an exponentially small type-II error at a fixed implementation error. A claim about noisy hardware requires its actual noise model and a corresponding statistical analysis.

The equality proved here is an equality of leading rates. It does not say that finite-copy risks, gate counts, numerical stability, or runtime are identical for every readout scheme. In particular, the fixed-block statement in [block_measurements.md](block_measurements.md) is a max–min information statement; it does not solve arbitrary stopping-time, adaptive quantum-memory bandit regret. [Ng, §§VI–VII](https://arxiv.org/html/2609.40339v1) separates the composite-testing question from that further learning reduction. The remaining boundaries are collected in [certification.md](certification.md).

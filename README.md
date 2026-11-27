# Quantum Bandit Certification

**Can quantum memory reduce exploration in a bandit whose arms supply unknown quantum states?** For a known common reward observable, separate spectral readout followed by classical KL-UCB attains the exact leading logarithmic regret, even against policies that retain and jointly measure every specimen.

## Use the reward readout

Use one supplied specimen at a time. Apply the compiled basis change for the known reward observable, measure in the computational basis and group outcomes with the same reward eigenvalue. Record the spectral label and release the register. The [qubit example](science/examples.md#states-and-reward) uses direct Z readout and counts outcome zero as reward one.

- **Certify a source.** Compute the expected spectral frequencies from the known reference. Count outcomes over the fixed copy budget and apply the [frequency distance test](science/certification.md#matching-spectral-test) to return one accept or reject decision.
- **Choose an arm.** Pull each arm once and keep a frequency table per arm. Compute the [empirical KL-UCB indices](science/adaptive_regret.md#4-an-attaining-policy), request a fresh specimen from an arm with the largest index and update its counts. The classical finite-support policy is due to Cappé et al. and was applied to spectral outcomes by Ng. [Related work](references/RELATED_WORK.md)

The sequential procedure retains classical counts between specimens. Charge preparation and delivery, the readout apparatus and resets, basis-change synthesis and the classical test or index calculation. The [resource account](science/resources.md#finite-precision-and-interpretation) gives the accumulated effect of finite readout error on the ideal-measurement guarantees.

Let $`F=\sum_i f_iP_i`$ be a known effect, $`\rho`$ a reference state, and $`\mathrm{Tr}(\rho F)\lt r\lt f_{\max}`$. An unknown source supplies independent copies of either $`\rho`$ or one fixed state $`\sigma`$ satisfying $`\mathrm{Tr}(\sigma F)\geq r`$. One test must work against every such alternative. Put

```math
p_i=\mathrm{Tr}(\rho P_i),\qquad
K=\min_{\substack{q\in\Delta_L\\\sum_iq_if_i\geq r}}D(p\Vert q).
```

For every fixed allowed Type-I error strictly between zero and one, the best worst-case Type-II error has exponent $`K`$, even with arbitrary collective measurements. Measuring $`F`$ spectrally on each copy attains this rate. The result permits every reference state, including pure states and zero spectral populations.

| Result | Consequence | Scientific account |
| --- | --- | --- |
| Exact adaptive regret coefficient | Spectral KL-UCB matches the optimum with arbitrary quantum memory | [Adaptive regret theorem](science/adaptive_regret.md) |
| Exact collective certification exponent | Independent reward readout attains the unrestricted rate | [Certification theorem](science/certification.md) |
| Strong converse and finite-confidence bounds | A larger exponential rate forces acceptance of the reference to vanish | [Finite-confidence proof](science/certification.md#exact-finite-confidence-converse) |
| Every fixed block has value $`V_m=K`$ | A common collective measurement on any finite number of copies cannot improve the worst-case KL rate per copy | [Block measurements](science/block_measurements.md) |
| Exact mixture measured divergence $`nK`$ | An explicit mixture of fixed IID alternatives defeats the apparent pairwise advantage | [Modular mixtures](science/modular_mixtures.md) |

The certification proof averages a family of states with the same better reward, each supplying one fixed IID source. The regret proof turns under-sampling an arm into a fixed-copy test. Smoothing the same phase family gives a finite set of better-arm replacements that transfers pointwise consistency to the test.

[Ng](https://arxiv.org/abs/2609.40339v1) established the single-copy spectral collapse and left the arbitrary-memory coefficient open. The [related-work account](references/RELATED_WORK.md) traces the fixed-sample results, the new adaptive converse and the inherited KL-UCB policy.

## Read the science

Start with the [model and exact claims](science/model.md), then the [connected reading route](science/README.md).

| Question | Account |
| --- | --- |
| What is known, supplied and returned? | [Model](science/model.md) |
| Why do collective certification tests lose their advantage? | [Certification proof](science/certification.md) |
| Why is a mixture of IID sources the right witness? | [Modular mixtures](science/modular_mixtures.md) |
| Why does every fixed measurement block have the same value? | [Block measurements](science/block_measurements.md) |
| What happens in a complete qubit experiment? | [Worked examples](science/examples.md) |
| How does the certificate constrain adaptive exploration? | [Adaptive regret proof](science/adaptive_regret.md) and [interpretation](science/interpretation.md) |
| Which physical and computational costs remain? | [Resources](science/resources.md) |
| What is established by the numerical checks? | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps the authoritative statements and proof routes.

## Learn the project

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's standard-layout manuscript. The [Watrous bridge](learning/WATROUS_BRIDGE.md) identifies precise source sections, translates notation and logarithm units, and supplies the steps connecting textbook foundations to this certification problem.

The [worked tutorial](learning/TUTORIAL.md) connects a 33-copy certificate to the exploration cost in a two-arm qubit bandit. The [30-milestone map](learning/MILESTONES.md) connects 12 background milestones to 18 milestones developing the contribution. The [learning overview](learning/README.md) joins these routes without requiring a cover-to-cover textbook reading.

## Reproduce the finite checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_science.py
```

The checks compare matrix constructions, support completion, classical optimization and binomial probabilities. Exact rational checks certify the two-arm qubit comparison and verify the reduced effect for a stopped measurement example.

## Scope

Certification fixes the dimension, reward observable, known reference and threshold as the copy budget grows. The regret theorem fixes a finite unknown-arm instance with independent specimens, classical arm requests, and best reward below the top eigenvalue. It compares leading expected pseudo-regret among pointwise-consistent policies.

Equality of leading exponents does not mean identical finite-copy error probabilities. All supplied copies, state preparation, coherent storage and measurement synthesis have physical costs. No QRAM, inverse preparation oracle, efficient arbitrary collective readout or hardware crossover is assumed.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

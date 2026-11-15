# Quantum Bandit Certification

**Can collective quantum measurements certify a source against every better-reward alternative more efficiently?** For a known reference state, a known reward observable and a fixed reward threshold, the optimal asymptotic confidence rate is exactly classical.

Let $`F=\sum_i f_iP_i`$ be a known effect, $`\rho`$ a reference state, and $`\mathrm{Tr}(\rho F)\lt r\lt f_{\max}`$. An unknown source supplies independent copies of either $`\rho`$ or one fixed state $`\sigma`$ satisfying $`\mathrm{Tr}(\sigma F)\geq r`$. One test must work against every such alternative. Put

```math
p_i=\mathrm{Tr}(\rho P_i),\qquad
K=\min_{\substack{q\in\Delta_L\\\sum_iq_if_i\geq r}}D(p\Vert q).
```

For every fixed allowed Type-I error strictly between zero and one, the best worst-case Type-II error has exponent $`K`$, even with arbitrary collective measurements. Measuring $`F`$ spectrally on each copy attains this rate. The result permits every reference state, including pure states and zero spectral populations.

| Result | Consequence | Scientific account |
| --- | --- | --- |
| Exact collective certification exponent | Independent reward readout attains the unrestricted rate | [Certification theorem](science/certification.md) |
| Strong converse and finite-confidence bounds | A larger exponential rate forces acceptance of the reference to vanish | [Finite-confidence proof](science/certification.md#exact-finite-confidence-converse) |
| Every fixed block has value $`V_m=K`$ | A common collective measurement on any finite number of copies cannot improve the worst-case KL rate per copy | [Block measurements](science/block_measurements.md) |
| Exact mixture measured divergence $`nK`$ | An explicit mixture of fixed IID alternatives defeats the apparent pairwise advantage | [Modular mixtures](science/modular_mixtures.md) |

The mechanism is a family of different states with the same better reward. Averaging their shared modular phase across the whole batch produces a feasible adversarial mixture. This does not change the source on every copy: each component is still one fixed IID source.

[Ng's single-copy spectral collapse](https://arxiv.org/abs/2609.40339v1) and the established relative-entropy and pinching tools are foundations. The contribution here is the all-copy certification theorem, its strong converse, the exact finite-block value and the support-complete mixture construction. [Related work](references/RELATED_WORK.md) separates these conclusions from the inherited ingredients.

## Read the science

Start with the [model and exact claims](science/model.md), then the [connected reading route](science/README.md).

| Question | Account |
| --- | --- |
| What is known, supplied and returned? | [Model](science/model.md) |
| Why do collective certification tests lose their advantage? | [Certification proof](science/certification.md) |
| Why is a mixture of IID sources the right witness? | [Modular mixtures](science/modular_mixtures.md) |
| Why does every fixed measurement block have the same value? | [Block measurements](science/block_measurements.md) |
| What happens in a complete qubit experiment? | [Worked examples](science/examples.md) |
| What does this say about quantum learning and bandits? | [Interpretation](science/interpretation.md) |
| Which physical and computational costs remain? | [Resources](science/resources.md) |
| What is established by the numerical checks? | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps the authoritative statements and proof routes.

## Learn the project

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's standard-layout manuscript. The [Watrous bridge](learning/WATROUS_BRIDGE.md) identifies precise source sections, translates notation and logarithm units, and supplies the steps connecting textbook foundations to this certification problem.

Start with the [worked tutorial](learning/TUTORIAL.md): one detector, a coherent reference qubit, a 33-copy certificate and the shared-phase obstruction to collective improvement. The [30-milestone map](learning/MILESTONES.md) connects 12 background milestones to 18 milestones developing the contribution. The [learning overview](learning/README.md) joins these routes without requiring a cover-to-cover textbook reading.

## Reproduce the finite checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_science.py
```

The checks compare independent matrix constructions, support completion, classical optimization and exact binomial probabilities. Universal conclusions follow from the analytical proofs. Finite checks do not establish a global optimization certificate or literature priority.

## Scope

Dimension, reward observable, reference and threshold are fixed while the copy budget grows. The reference is known for certification; the theorem does not supply a complete learner for an unknown bandit arm. The finite-block statement concerns one common finite-outcome measurement and a worst-case information rate. Optimal regret for unrestricted adaptive quantum-memory bandit policies remains unproved.

Equality of leading exponents does not mean identical finite-copy error probabilities. All supplied copies, state preparation, coherent storage and measurement synthesis have physical costs. No QRAM, inverse preparation oracle, efficient arbitrary collective readout or hardware crossover is assumed.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

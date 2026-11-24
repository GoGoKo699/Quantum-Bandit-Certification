# From Watrous to quantum bandit certification and regret

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018), the author's standard-layout manuscript**. Use the [author's book page](https://jhwatrous.github.io/books-and-courses.html) and its [standard-layout copy](https://jhwatrous.github.io/TQI.pdf). Page numbers below are the numbers printed in that manuscript. The linked book remains with its author; this repository supplies its own explanations and research proofs.

Start with the [complete qubit experiment](../science/examples.md). A source sends qubits. The reference is known, and the alternative may be any fixed state whose reward is higher. Separate reward readouts certify the source using one count. The central question is whether retaining the qubits and measuring them together improves the leading confidence rate.

Keep the two error probabilities visible: Type I rejects the reference when it is true; Type II accepts the reference when a better-reward alternative is true. One common test controls the worst Type-II probability across the whole alternative family. The adaptive bandit result uses that fixed-sample theorem to bound an event in a different experiment, where the learner must choose among unknown sources.

## A selective reading route

Read the relevant passages when the corresponding object enters the story. The [30-milestone map](MILESTONES.md) organizes the project rather than following the book from beginning to end.

| Passage in the selected manuscript | Purpose in this project | Continue in the scientific account |
| --- | --- | --- |
| §2.1.2, p.61; §§2.3.1–2.3.2, pp.100–112. Definition2.34 and Eq.(2.201), p.101. | Represent a specimen by a density operator and turn a measurement into an ordinary outcome distribution. | [Inputs and hypotheses](../science/model.md#supplied-information-and-hypotheses) |
| §1.1.2, p.8, and §1.1.3, p.24 onward. | Read projections, tensor products, spectral powers and operator logarithms when they appear in the proof. | [Classical quantity](../science/model.md#the-classical-quantity) and [modular notation](../science/modular_mixtures.md#setting-and-inherited-tools) |
| §1.2.1, p.35, and §1.2.2, p.47 onward. | Interpret convex mixtures, minimization and repeated independent observations. | [One shared source choice](../science/interpretation.md#what-the-source-model-permits) |
| §3.1.1, pp.125–131; Theorem3.4 and the convex-family discussion in Scenario3.6/Theorem3.7. | Separate a measurement designed for one known pair from a measurement that must handle an unknown member of a family. | [Pairwise gap in the qubit example](../science/examples.md#where-the-apparent-collective-advantage-goes) |
| §§5.1.1–5.1.2, pp.250–264. | Understand classical relative entropy and why processing an outcome record cannot increase its information. | [Spectral rate](../science/model.md#the-classical-quantity) and [matching frequency test](../science/certification.md#matching-spectral-test) |
| §§5.2.1–5.2.3, pp.265–282; Theorem5.35, p.280. | Read quantum relative entropy, its support condition and its decrease under a channel, including measurement. | [Two mixture divergences](../science/modular_mixtures.md) |
| §4.1.1, Definition4.4, p.203, and Proposition4.6, p.204. | View pinching as removing coherence between specified blocks by averaging unitary phases or forgetting a projective measurement record. | [Feasible pinched mixture](../science/certification.md#a-feasible-mixture-on-every-tensor-power) |
| §§2.2–2.3 and §1.2. | Use a fixed quantum apparatus to represent an event by a single effect, and compactness to choose finitely many positive operator comparisons. | [Adaptive regret](../science/adaptive_regret.md) |

The probability bounds, empirical-type argument and variational log-derivative calculation needed after these passages are supplied in the project files. They are not left as unstated prerequisites.

## Translate the notation before transferring a result

| Watrous notation or convention | Notation here | Meaning to retain |
| --- | --- | --- |
| A complex Euclidean space, often $`\mathcal X`$ | $`\mathcal H`$ or $`\mathbb C^d`$ | The finite-dimensional state space of one specimen. |
| $`\mathrm{Pos}(\mathcal X)`$, $`\mathrm{D}(\mathcal X)`$ | Positive semidefinite operators; density operators such as $`\rho,\sigma`$ | A state is positive and has trace one; a filtered intermediate operator may have smaller trace. |
| Measurement operator $`\mu(a)`$ | $`M_a`$; for a binary decision, $`T_n,I-T_n`$ | The probability of outcome $`a`$ is $`\mathrm{Tr}(M_a\rho)`$. Here $`\mu`$ instead denotes the reference's reward mean. |
| Identity $`1_{\mathcal X}`$ and adjoint $`A^*`$ | $`I`$ and $`A^\dagger`$ | These are notation changes only. |
| A pinching channel $`\Phi`$ | $`\mathcal E_n`$ | The blocks here are eigenspaces of the tensor-product ratio operator $`W_n`$. |
| Base-two $`\log`$ and entropy in bits | Natural $`\log`$ and rates in nats | Multiply a book relative entropy by $`\ln2`$ to obtain this project's convention. |
| Fidelity, denoted $`F`$ in the book | The reward effect $`F`$ here | The project symbol is an observable with $`0\leq F\leq I`$, not a fidelity. |

In particular,

```math
D_{\rm project}(p\Vert q)=(\ln2)D_{\rm book}(p\Vert q),\qquad
D_{\rm project}(\rho\Vert\sigma)=(\ln2)D_{\rm book}(\rho\Vert\sigma).
```

The qubit value $`K=0.8303656034\ldots`$ is in nats per supplied copy. Mixing logarithm conventions changes that number, although it does not change which test is optimal.

## The bridge from textbook foundations to the new mechanism

First, use the measurement rule to obtain $`p_i=\mathrm{Tr}(\rho P_i)`$ from the reward's spectral measurement. Every better-reward state produces a feasible classical vector $`q`$. The closest such vector, $`q^*`$, defines the spectral rate $`K=D(p\Vert q^*)`$. This is where the quantum experiment first acquires an entirely classical description.

Next, return to the quantum state rather than discarding its coherence. On the populated reward eigenspaces, the ratios $`p_i/q_i^*`$ define a positive operator $`\Omega_S`$. Filtering $`\rho`$ by this operator and rotating its phase generates states with the same populations $`q^*`$. If $`q^*`$ puts probability outside the reference's populated eigenspaces, a fixed complementary block supplies it. That filtered block is allowed to be subnormalized; renormalizing it would change the alternative and the proof.

The decisive many-copy object is a mixture of $`\sigma_t^{\otimes n}`$ with **the same phase parameter on every copy**. Each component is still one fixed IID source. Binary acceptance probabilities are linear, so a mixture of valid alternatives supplies a valid worst-case lower bound. Taking independent phases on different copies would describe a different experiment.

Two averages have different jobs:

| Feasible average | Role in the proof |
| --- | --- |
| Logistic modular average $`\zeta_n`$ | The logarithm derivative and a concave variational objective give the exact identity $`D_M(\rho^{\otimes n}\Vert\zeta_n)=nK`$. |
| Cesaro phase average $`\eta_n`$ | Pinching gives a lower bound on every test's worst-case error and an Umegaki divergence within $`\log v_n`$ of $`nK`$. |

The book's pinching definition makes the second construction recognizable. The proof then uses the pinching inequality in its actual direction, $`R_n\leq v_n\mathcal E_n(R_n)`$, counts the spectral blocks and controls an ordinary IID tail. At fixed dimension, the block count grows polynomially, so it does not improve an exponential confidence rate. This yields the strong converse: a rate above $`K`$ forces the probability of accepting the reference to vanish.

Finally, fix a finite collective block measurement and repeat it. If its worst-case KL information per copy exceeded $`K`$, a classical frequency test on repeated block outcomes would violate the certification theorem. This proves the [fixed-block equality](../science/block_measurements.md). The argument does not replace a mixture's KL divergence with that of one component or exchange the order of the optimizations.

## Apply the fixed-sample bound to an adaptive policy

The bandit arms supply copies of unknown states, one copy for each classical arm request. The policy may choose the next request using an instrument on all stored quantum systems. Fix an arm and a cutoff $`m`$. The experiment that runs the policy but rejects when it requests specimen $`m+1`$ of that arm is a binary test on the $`m`$ specimens. Fixed registers for the remaining arms and the policy's workspace are part of the apparatus. This step uses the textbook measurement rule and channel composition to represent the cutoff event by one effect.

Pointwise consistency constrains the policy on any fixed replacement instance for which the modified arm is strictly best. Mixing each member of the higher-reward phase family with a small maximally mixed component keeps the replacement strictly better and makes positive operator comparisons stable. A fixed finite cover then transfers the probability bounds from finitely many such instances to the phase average, with an arbitrarily small exponent loss per copy. The pinching bound forces the required logarithmic pulls. The [adaptive regret proof](../science/adaptive_regret.md) develops this use of the phase witness and its matching leading coefficient.

## What is supplied by which source

Watrous supplies the selected educational foundation: states, measurements, discrimination language, relative entropy and pinching channels. The research literature supplies additional tools and the earlier single-copy spectral collapse; [Related work](../references/RELATED_WORK.md) records those attributions. In particular the measured-relative-entropy variational formula and the modular logarithm-derivative representation are research-level proof ingredients explained in [Modular mixtures](../science/modular_mixtures.md).

The project's added conclusions are the support-complete many-copy construction, the exact mixture divergences, the uniform certification rate and its strong converse, the fixed-block information value, and the adaptive quantum-memory regret converse. The matching spectral KL-UCB policy and the states-as-arms model come from Ng and the classical bandit literature.

## Continue through the project

Use [M01–M12](MILESTONES.md) to connect individual specimens, outcomes, information and uncertainty into the certification task. The settled narrative then follows this route:

| Milestones in the common map | Connection to follow |
| --- | --- |
| M13–M17 | Begin with the coherent qubit, find the closest populations, complete missing support and keep one shared phase across the batch. |
| M18–M20 | Connect the logarithm derivative, common lower witness and stationarity into the exact measured-divergence identity. |
| M21–M25 | Switch to the pinched mixture, control sectors and likelihood tails, match the strong converse with a spectral test, and evaluate the regularized quantum expression. |
| M26–M27 | Transfer the certification rate by block repetition and identify the threshold and error endpoints. |
| M28–M30 | Test a cutoff on the number of pulls, control the phase family using a fixed finite cover, and derive the optimal logarithmic regret. |

The fixed-sample theorem uses a known reference, a fixed finite dimension and threshold, an unknown fixed IID alternative, and a positive Type-I tolerance. The bandit result uses unknown fixed IID arms, a known reward effect, classical arm requests, and pointwise consistency. Each result fixes the instance before its asymptotic limit.

Return to the [33-copy qubit experiment](../science/examples.md#a-finite-confidence-test) for a count with explicit error guarantees. The [adaptive theorem](../science/adaptive_regret.md) gives the corresponding exploration requirement in the unknown-arm setting. The [resource account](../science/resources.md) prices supplied copies, readout, and storage.

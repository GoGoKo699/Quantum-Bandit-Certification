# When coherent specimens do not improve a uniform certificate

Suppose a laboratory source is promised to be one of two things. It is either a known reference source, or it is an unknown source whose mean reward is much higher. A measurement can inspect the specimens one at a time. A quantum apparatus could instead keep them and perform one joint measurement. The question is whether the second apparatus can make its error decrease faster as more specimens arrive.

The answer for the full better-reward family is exact: separate spectral readout already has the optimal leading confidence rate. Understanding why requires keeping **one common test against a whole family** separate from a test designed for one known pair of states.

This explanation follows the settled [30-milestone map](MILESTONES.md). M01–M12 assemble the task's foundations; M13–M30 develop the example, two shared-phase witnesses, matched certificate, and learning boundary. The sole educational anchor is Watrous, *The Theory of Quantum Information* (2018), using the author's standard-layout manuscript. The [source bridge](WATROUS_BRIDGE.md) identifies the relevant passages and separates those foundations from the research ingredients supplied here.

## One detector and a complete qubit experiment

A qubit has two reward-basis states, $`|0\rangle`$ and $`|1\rangle`$. The detector reports reward one for the first outcome and zero for the second. Its reward operator is $`F=|0\rangle\langle0|`$.

The known reference is

```math
\rho=\begin{pmatrix}1/2&9/20\\9/20&1/2\end{pmatrix}
=0.95|+\rangle\langle+|+0.05|-\rangle\langle-|,
\qquad |\pm\rangle=\frac{|0\rangle\pm|1\rangle}{\sqrt2}.
```

Its diagonal entries say that reward readout gives one with probability one half. The off-diagonal entries contain coherence: a different measurement can reveal information that reward readout discards. For example, measuring in the $`|+\rangle,|-\rangle`$ basis gives probabilities $`0.95`$ and $`0.05`$.

The alternative may be **any fixed qubit state** $`\sigma`$ for which the probability of reward one is at least $`0.95`$. Within an experiment, every specimen is independently prepared in the same state. There is no source drift or entangled input batch. The experiment supplies either $`\rho^{\otimes n}`$ or $`\sigma^{\otimes n}`$.

The tester returns one binary decision. A Type-I error rejects the reference when the source really is the reference. A Type-II error accepts the reference when the source is a better-reward alternative. The latter must be controlled for every allowed $`\sigma`$. Acceptance is a certificate for this promised comparison; it is not tomography or proof that the source equals $`\rho`$ among all conceivable low-reward states.

The classical description of $`\rho`$ is already supplied. This is a known-reference certification task, rather than a learner obtaining that description from uncharged training data. These distinctions form M01–M05, M08, M12, and M13.

## Run a certificate with 33 specimens

Measure the reward basis on each specimen and count the ones. Accept the reference if there are at most $`26`$ ones among $`33`$ specimens; otherwise reject it.

Under the reference, this is an ordinary binomial count with success probability $`0.5`$. Under an alternative, the success probability is at least $`0.95`$. The chance of obtaining so few ones is largest at the boundary $`0.95`$ and decreases for larger success probabilities.

| Error of this particular test | Exact binomial probability, numerically evaluated | Chernoff upper guarantee |
| --- | --- | --- |
| Reject the reference when it is true | $`0.0001620317\ldots`$ | Less than $`0.00173`$ |
| Accept a better-reward alternative, worst case | $`0.0010550611\ldots`$ | Less than $`0.00993`$ |

Both errors are below one percent. The apparatus needs one incoming qubit at a time and one classical count. The [complete example](../science/examples.md#a-finite-confidence-test) supplies the exact sums, the Chernoff calculation, and a sufficient-copy formula for other confidence targets. [Verification](../verification/README.md) reproduces the numerical values.

These numbers concern a concrete finite test. They do not establish that 33 is the smallest possible budget or that all joint and separate tests have identical finite-copy risks. M09 and M24 connect this usable certificate to the leading-rate theorem.

## What the exact rate means

For two Bernoulli distributions, define the directional relative entropy

```math
\mathrm{kl}(p,q)
=p\log\frac pq+(1-p)\log\frac{1-p}{1-q}.
```

The null probability comes first. With natural logarithms, the qubit's rate is

```math
K=\mathrm{kl}(0.5,0.95)
=\frac12\log\frac{100}{19}
=0.8303656034\ldots
```

An error exponent describes the leading value of $`-\log\beta_n/n`$, where $`\beta_n`$ is the worst Type-II probability. A larger exponent means faster exponential decay. It is not a formula setting a finite risk equal to $`e^{-nK}`$.

The theorem permits every collective quantum test. For any fixed positive Type-I tolerance smaller than one, the optimal worst-case Type-II exponent is $`K`$. Separate reward measurements attain that rate. If a sequence of collective tests tries to exceed it, its probability of accepting the true reference tends to zero. This last conclusion is the strong converse.

For a general known effect $`F=\sum_i f_iP_i`$, keep its complete spectral outcome, with probabilities $`p_i=\mathrm{Tr}(\rho P_i)`$. The answer becomes

```math
K=\min_{\substack{q\in\Delta_L\\\sum_iq_if_i\ge r}}D(p\Vert q).
```

The minimization chooses the alternative reward-population vector closest to the reference. All parameters, including dimension, are fixed before the number of copies grows. The [model](../science/model.md) states the exact quantifiers; M06, M08, and M23 explain their roles.

## Why coherence initially seems promising

If both states were completely known, a joint quantum measurement could be designed for that particular pair. Its asymptotic information is described by quantum relative entropy $`D(\rho\Vert\sigma)`$. This can exceed the divergence left after reward readout.

For the qubit above, the closest pointwise quantum relative-entropy distance to the better-reward halfspace is numerically about $`1.11733005`$, larger than $`K`$. This inherited numerical comparison is recorded in the [scientific example](../science/examples.md#where-the-apparent-collective-advantage-goes). It is not a number needed by the proof.

The difficulty is operational. The measurement that uses a known alternative's coherence may depend on which alternative it is. A certificate has to work before receiving that identity. A larger information distance for every individually optimized pair does not automatically provide one common apparatus at that rate. M07 and M13 make this distinction precise.

## Build the family that obstructs a common apparatus

In the qubit experiment, the closest classical alternative has reward populations $`(0.95,0.05)`$. It can still have different coherences. One useful family is

```math
\sigma_\theta=
\begin{pmatrix}
0.95&c e^{i\theta}\\
c e^{-i\theta}&0.05
\end{pmatrix},
\qquad c=\frac{9\sqrt{19}}{200}.
```

Every member is a positive, normalized state with reward exactly $`0.95`$. Changing the phase $`\theta`$ changes the quantum alternative without moving its reward populations. This family is obtained by filtering the reference with the classical population ratios and then rotating a phase. The [example](../science/examples.md#the-physical-alternative-orbit) gives the exact operator formula; M14–M16 explain how the same construction works for general rewards.

Now imagine choosing one phase at the beginning of an experiment and keeping it for all $`n`$ specimens. Conditional on that choice, the source is still the valid IID source $`\sigma_\theta^{\otimes n}`$. A test that rejects every member of the family must also reject their average: its acceptance probability is linear in the input density operator.

This averaging is a proof device. It does not give the tester a phase record, allow the physical source to change between copies, or replace the uniform guarantee with a test for only one averaged state.

## A shared phase preserves some joint coherence

It matters that the same phase is used across the batch. With two specimens, the matrix entry connecting $`|01\rangle`$ and $`|10\rangle`$ is

```math
\langle01|\sigma_\theta^{\otimes2}|10\rangle
=(ce^{i\theta})(ce^{-i\theta})=c^2.
```

The phases cancel, so this joint coherence survives a uniform common-phase average. If a fresh independent phase were averaged separately for each specimen, each single-copy off-diagonal entry would disappear and this tensor entry would be zero.

The valid many-copy witness therefore retains structure that independent dephasing would erase. The proof handles that remaining structure rather than silently introducing a more destructive source model. This is the key connection in M17.

## Two averages have different jobs

The proof uses the same family of valid alternatives in two ways.

| Average over the shared phase | What it establishes |
| --- | --- |
| A particular logistic weighting, denoted $`\zeta_n`$ | The exact finite-copy identity $`D_M(\rho^{\otimes n}\Vert\zeta_n)=nK`$ for measured relative entropy. |
| A long-time uniform average, denoted $`\eta_n`$ | A pinching witness that bounds every test and proves the fixed-error strong converse. |

Measured relative entropy $`D_M`$ is the largest classical relative entropy obtainable by measuring a known pair. For the logistic witness, the averaged active block equals a derivative of the matrix logarithm. An inherited variational formula turns that derivative identity into a concave optimization whose stationary point has value $`nK`$. Classical optimality also supplies the matching lower bound for every feasible mixture. M18–M20 and [Modular mixtures](../science/modular_mixtures.md) supply these steps explicitly.

The uniform average has a different advantage: it keeps exactly the blocks with equal total spectral log-ratio. This operation is called pinching. For the binary experiment, there are at most $`n+1`$ such blocks, indexed by the number of occurrences of a reward sector. For a general fixed spectrum, the number remains polynomial in $`n`$.

Writing $`R_n=\rho^{\otimes n}`$, the useful comparison is

```math
R_n\le v_n\mathcal E_n(R_n),
```

where $`\mathcal E_n`$ is pinching and $`v_n`$ counts its blocks. Consequently any test that accepts the reference with appreciable probability must also accept enough of the pinched reference. The alternative witness rescales those blocks by products of the classical ratios $`q_i^*/p_i`$.

Under the reference, the logarithm of the inverse rescaling is a sum of independent random variables. Its mean is $`nK`$, and its upper tail is controlled by an ordinary concentration bound. Together these facts give

```math
\beta_n\ge e^{-nc}
\left[\frac{a_n}{v_n}-u_n(c)\right]_+.
```

Here $`a_n`$ is null acceptance, $`u_n(c)`$ is the upper-tail probability of that classical log-ratio sum, and $`[x]_+=\max\{x,0\}`$. For $`c>K`$, the tail vanishes exponentially. A polynomial block penalty cannot compensate for an attempted strictly larger exponential confidence rate. This is the causal step behind the strong converse, developed in M21–M23 and proved in [Certification](../science/certification.md#exact-finite-confidence-converse).

The same pinched witness has quantum relative entropy $`nK`$ plus a coherence remainder of at most $`\log v_n`$. That remainder disappears per copy. M25 explains how this evaluates the regularized mixture expression, rather than identifying it with the larger distance to one fixed alternative.

## Missing null populations must remain missing

The construction also covers pure reference states and reward sectors that the reference never occupies. It does so by preserving probability mass, rather than dividing by zero or normalizing an intermediate block incorrectly.

For a concrete three-sector example, take reward values $`(0,0.5,1)`$, reference populations $`p=(0.6,0.4,0)`$, and threshold $`r=0.8`$. The closest alternative vector is

```math
q^*=(0.12,0.16,0.72).
```

Filtering on the two populated reference sectors produces a positive block with diagonal $`(0.12,0.16)`$ and trace $`0.28`$. It is deliberately subnormalized. The remaining $`0.72`$ is added in the third, null-orthogonal sector. The completed state is normalized and has reward $`0.5(0.16)+0.72=0.8`$.

Normalizing the first block on its own would discard the very population needed to meet the reward constraint. M15 and M27 explain why this support completion is essential; the [canonical proof](../science/certification.md#classical-optimizer-and-null-support) treats arbitrary spectral degeneracy and null rank.

## Why no fixed collective block escapes the result

Suppose a joint measurement on a fixed block of $`m`$ copies had worst-case classical KL information per copy larger than $`K`$. Repeat that same measurement on many independent blocks. Each block returns one of finitely many classical outcomes. A frequency test on those outcomes would then certify the reference at a rate above $`K`$, contradicting the established collective converse.

Thus every finite block has optimal common-measurement value $`K`$. This is a repetition argument, not an exchange of the measurement and alternative optimizations. Divergence to a mixture can be smaller than divergence to every component, so the exact mixture identity alone would not justify that exchange. M26 and [Block measurements](../science/block_measurements.md) preserve this distinction.

## What this establishes about learning

The known-reference certificate is a component of the states-as-arms quantum bandit problem. The result establishes its optimal uniform rate and the value of every fixed finite measurement block. An unknown-arm learner with adaptive allocations, stopping times, and retained quantum memory asks a further question. The present fixed-sample theorem does not by itself determine that learner's optimal regret coefficient.

Its statistical scope also matters. The alternative family is the full reward halfspace. A smaller calibrated family can permit different measurements and different gains. The theorem uses a fixed positive Type-I tolerance; demanding exactly zero Type-I error is a different constraint. Thresholds that include the null or reach the reward's maximal eigenspace have their own [endpoint conclusions](../science/certification.md#endpoint-cases).

Separate readout attains the rate with supplied specimens and classical counts. Preparing those specimens and measuring a generic dense reward may still be expensive. Equality of leading rates does not establish equal finite risks, runtime, energy, or robustness to fixed hardware error. M28–M30 connect these costs and limits to the [resource account](../science/resources.md) and [scientific interpretation](../science/interpretation.md).

Watrous supplies the language of states, measurements, discrimination, relative entropy, and pinching. The logarithmic-derivative variational tools and the earlier single-copy collapse come from the attributed research literature. The support-complete shared-phase constructions, matched collective certificate, and finite-block consequence are developed in the project's scientific account. The [source bridge](WATROUS_BRIDGE.md) gives precise reading locations and keeps these roles distinct.

# The certification task and its exact limits

A quantum bandit arm emits a state, and a known observable assigns that state a mean reward. Before making a claim about the value of retaining quantum examples, one must distinguish a pairwise discrimination problem from a certificate that handles every state with a better reward. This project solves the latter fixed-sample task and its finite-block information game.

## Supplied information and hypotheses

Fix a finite-dimensional Hilbert space and a known effect

```math
0\leq F\leq I,\qquad F=\sum_{i=1}^{L}f_iP_i,
```

where the eigenvalues are distinct and the spectral projections may be degenerate. Any bounded Hermitian reward can be put in this form by an affine change of scale. The reference state $`\rho`$ and threshold $`r`$ are known to the tester. Define

```math
p_i=\operatorname{Tr}(\rho P_i),\qquad
\mu=\operatorname{Tr}(\rho F),\qquad
\Lambda_r=\{\sigma\geq0:\operatorname{Tr}\sigma=1,
                        \operatorname{Tr}(\sigma F)\geq r\}.
```

The nontrivial regime is $`\mu\lt r\lt f_{\max}`$. No rank assumption is imposed on $`\rho`$. The source supplies $`n`$ fresh independent copies of either the reference or one unknown fixed $`\sigma\in\Lambda_r`$. The source's preparation circuit, inverse and purifying environment are not supplied.

A tester returns one binary decision. Its effect $`T_n`$ accepts the reference, and

```math
\alpha_n=1-\operatorname{Tr}(\rho^{\otimes n}T_n),\qquad
\beta_n=\sup_{\sigma\in\Lambda_r}
               \operatorname{Tr}(\sigma^{\otimes n}T_n).
```

The supremum requires a single test to handle the entire alternative set. The maximizing state may depend on the test and on $`n`$; within any experiment all copies come from the same state. A mixture of tensor powers is legitimate for proving a minimax lower bound because a test's acceptance probability is linear in the alternative density operator.

## The classical quantity

Write

```math
Q_r=\{q\in\Delta_L:\textstyle\sum_iq_if_i\geq r\},\qquad
K=\min_{q\in Q_r}D(p\Vert q),
\qquad
D(p\Vert q)=\sum_{i:p_i>0}p_i\log\frac{p_i}{q_i}.
```

Logarithms are natural, so rates are in nats per copy. Every feasible vector $`q`$ is realized by a state, for example $`\sum_iq_iP_i/\operatorname{rank}P_i`$. Measuring the spectral projectors of $`F`$ therefore produces exactly the classical composite experiment with null distribution $`p`$ and alternatives $`Q_r`$.

The minimum exists and is finite and positive in the nontrivial regime. Its optimizer may put probability in eigenspaces with zero null population; the [support construction](certification.md#classical-optimizer-and-null-support) retains that probability explicitly. For projector rewards with null success probability $`p\lt r\lt1`$,

```math
K=p\log\frac p r+(1-p)\log\frac{1-p}{1-r},
```

with the usual zero-probability convention.

## Exact certification theorem

For $`0\lt\varepsilon\lt1`$, define

```math
\beta_n^*(\varepsilon)=
\inf_{\substack{0\leq T_n\leq I\\\alpha_n\leq\varepsilon}}
\sup_{\sigma\in\Lambda_r}\operatorname{Tr}(\sigma^{\otimes n}T_n).
```

Then

```math
\lim_{n\to\infty}-\frac1n\log\beta_n^*(\varepsilon)=K.
```

There are spectral-measurement tests with vanishing Type-I error attaining every rate below $`K`$. Conversely, if a sequence of arbitrary collective tests has $`\liminf_n[-\log\beta_n/n]>K`$, its probability of accepting the reference tends to zero. The [proof](certification.md) gives finite-confidence inequalities and all support boundaries.

The matching statement requires a positive error tolerance; exact zero Type-I error is a different constraint. For example, a full-rank reference forces $`T_n=I`$ if $`\alpha_n=0`$, giving exponent zero. The [endpoint table](certification.md#endpoint-cases) treats the trivial and top-eigenspace threshold regimes separately.

## Exact finite-block information value

For a positive integer $`m`$, define

```math
V_m=\sup_{M}\inf_{\sigma\in\Lambda_r}
\frac1mD\!\left(M(\rho^{\otimes m})\middle\Vert
                     M(\sigma^{\otimes m})\right),
```

where $`M`$ is one finite-outcome POVM, common to the whole alternative set. Then $`V_m=K`$ for every $`m\geq1`$. This theorem allows any finite number of copies within one coherent block. Its [repetition proof](block_measurements.md) does not exchange the order of the optimizations.

In particular this value differs conceptually from

```math
K^{(m)}=\frac1m\inf_{\sigma\in\Lambda_r}
 D_M(\rho^{\otimes m}\Vert\sigma^{\otimes m}),
```

where the measurement inside $`D_M`$ may depend on the alternative. A larger value of this latter envelope does not establish any achievable common-measurement advantage.

## Mixture identities

For $`C_n=\operatorname{conv}\{\sigma^{\otimes n}:\sigma\in\Lambda_r\}`$, the [modular-mixture construction](modular_mixtures.md) proves

```math
\inf_{\eta\in C_n}D_M(\rho^{\otimes n}\Vert\eta)=nK.
```

and constructs a possibly different mixture with

```math
nK\leq\inf_{\eta\in C_n}D(\rho^{\otimes n}\Vert\eta)
\leq nK+\log\binom{n+J-1}{J-1},
```

where $`J`$ is the number of distinct active spectral ratios $`p_i/q_i^*`$. The logarithmic remainder vanishes per copy at fixed dimension. The two mixtures serve different purposes: a logistic modular average gives the exact measured divergence, while a pinched orbit average gives the strong converse and the Umegaki bound.

## Limits relevant to learning

All asymptotics fix the instance first. A dimension-uniform high-precision sample frontier, noisy-memory theorem, efficient collective apparatus and optimal unrestricted adaptive bandit regret are not established. The [interpretation](interpretation.md) explains the surviving learning consequence; the [resource account](resources.md) includes acquisition, storage, control and output costs.

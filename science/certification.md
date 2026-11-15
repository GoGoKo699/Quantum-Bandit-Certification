# Uniform certification and finite-confidence bounds

The certification theorem does not require a full-rank null state or positive weight in every eigenspace of the reward. This chapter proves the uniform certification theorem, including its finite-confidence bounds and endpoint cases. It concerns fixed-sample certification and finite measurement blocks; it does not assert an optimal regret coefficient for unrestricted adaptive quantum-memory policies.

## Model and statement

Let $`F=\sum_{i=1}^{L}f_iP_i`$ be the spectral decomposition of a fixed effect on a finite-dimensional Hilbert space, with distinct eigenvalues $`f_i`$. Let $`\rho`$ be any density operator and write

```math
p_i=\mathrm{Tr}(\rho P_i),\qquad
\mu=\sum_i p_i f_i,\qquad f_{\max}=\max_i f_i.
```

For a threshold $`r`$, define the alternative set and its classical image by

```math
\Lambda_r=\{\sigma:\mathrm{Tr}(\sigma F)\geq r\},\qquad
Q_r=\{q\in\Delta_L:\textstyle\sum_iq_if_i\geq r\}.
```

Unless an endpoint is explicitly discussed, assume $`\mu\lt r\lt f_{\max}`$. Let

```math
K=\min_{q\in Q_r}D(p\Vert q),\qquad
D(p\Vert q)=\sum_{i:p_i>0}p_i\log\frac{p_i}{q_i}.
```

All logarithms are natural. A positive numerator with zero denominator contributes infinity. A zero numerator contributes zero.

For an acceptance effect $`0\leq T_n\leq I`$ for the null $`\rho^{\otimes n}`$, set

```math
a_n=\mathrm{Tr}(\rho^{\otimes n}T_n),\qquad
b_n=\sup_{\sigma\in\Lambda_r}
       \mathrm{Tr}(\sigma^{\otimes n}T_n).
```

For every fixed $`\varepsilon\in(0,1)`$, the optimal worst-case Type-II probability subject to $`a_n\geq1-\varepsilon`$ has exponent exactly $`K`$:

```math
\lim_{n\to\infty}-\frac1n\log
\inf_{\substack{0\leq T_n\leq I\\a_n\geq1-\varepsilon}}b_n=K.
```

The converse is strong: if the worst-case Type-II exponent is strictly greater than $`K`$, the null acceptance tends to zero. Measuring the spectral projectors of $`F`$ separately on each copy achieves $`K`$. Thus unrestricted collective measurements do not improve this certification exponent, including when some $`p_i`$ vanish or $`\rho`$ is pure.

## Classical optimizer and null support

The feasible simplex is compact and the divergence is lower semicontinuous, so an optimizer $`q^*`$ exists. The minimum is finite: mixing $`p`$ with a top-eigenvalue point mass gives a feasible vector that remains positive wherever $`p_i>0`$, because $`r\lt f_{\max}`$. Consequently every optimizer satisfies $`q_i^*>0`$ wherever $`p_i>0`$. Also $`K>0`$: a zero minimum would force $`q^*=p`$, contradicting $`r>\mu`$.

Define

```math
S=\{i:p_i>0\},\qquad
\Gamma=\sum_{i\in S}P_i,\qquad
\Omega_S=\sum_{i\in S}\frac{p_i}{q_i^*}P_i.
```

The operator $`\Omega_S`$ is strictly positive on $`\Gamma\mathcal H`$. Since $`\rho\geq0`$, a zero value of $`\mathrm{Tr}(\rho P_i)`$ implies $`P_i\rho=\rho P_i=0`$. Hence $`\rho=\Gamma\rho\Gamma`$. Inverses below are taken only on $`\Gamma\mathcal H`$; no inverse of a zero endpoint weight is used.

Set

```math
\chi=\Omega_S^{-1/2}\rho\Omega_S^{-1/2},\qquad
s=\mathrm{Tr}\chi=\sum_{i\in S}q_i^*,\qquad
\tau=\sum_{i\notin S}q_i^*\frac{P_i}{\mathrm{rank}P_i}.
```

The operators $`\chi`$ and $`\tau`$ have orthogonal supports and traces $`s`$ and $`1-s`$. The case $`\tau=0`$ is allowed. For real $`t`$, define the normalized state

```math
\sigma_t=
\Omega_S^{-it/2}\chi\Omega_S^{it/2}\oplus\tau.
```

Its spectral population vector for $`F`$ is exactly $`q^*`$: modular rotations commute with every active $`P_i`$, while $`\tau`$ supplies precisely the missing populations. Therefore $`\sigma_t\in\Lambda_r`$ for every $`t`$. This construction works for an arbitrary optimizer; it does not require locating its zero eigenvalues by a separate Karush–Kuhn–Tucker analysis or assuming missing probability enters only the top eigenspace.

## A feasible mixture on every tensor power

Write $`R_n=\rho^{\otimes n}`$, $`W_n=\Omega_S^{\otimes n}`$, and let $`\mathcal E_n`$ be pinching into the eigenspaces of $`W_n`$ on $`(\Gamma\mathcal H)^{\otimes n}`$. Define a normalized feasible mixture by the Cesaro limit

```math
\eta_n=\lim_{A\to\infty}\frac1A\int_0^A
           \sigma_t^{\otimes n}\,dt.
```

The limit exists in finite dimension: each matrix entry is a finite sum of constant or oscillatory exponential terms. It lies in

```math
C_n=\mathrm{conv}\{\sigma^{\otimes n}:\sigma\in\Lambda_r\}.
```

Indeed every finite-time average lies in this compact convex hull, which is closed. The mixture has no offdiagonal block between $`\Gamma^{\otimes n}`$ and its orthogonal complement, because each $`\sigma_t`$ is already block diagonal. Its null-support block is

```math
\Gamma^{\otimes n}\eta_n\Gamma^{\otimes n}
=\mathcal E_n(\chi^{\otimes n})
=W_n^{-1}\mathcal E_n(R_n).
```

The other blocks are positive and may be discarded in a lower bound on an acceptance probability. This is the support step that allows $`s\lt1`$; replacing $`\chi`$ by a normalized state would lose the factor that supplies the correct exponent.

Let $`v_n`$ be the number of distinct eigenvalues of $`W_n`$. If $`J`$ is the number of distinct eigenvalues of $`\Omega_S`$, then

```math
v_n\leq\binom{n+J-1}{J-1}.
```

This is polynomial in $`n`$ for a fixed input effect and dimension. The pinching inequality has its usual direction:

```math
R_n\leq v_n\mathcal E_n(R_n).
```

No reverse pinching inequality is used.

## Exact finite-confidence converse

Let $`Z`$ be the bounded classical random variable that equals $`\log(p_i/q_i^*)`$ with probability $`p_i`$, for $`i\in S`$. Its mean is $`K`$. For a real $`c`$, put

```math
u_n(c)=\Pr\!\left[\sum_{j=1}^n Z_j>nc\right],
```

where the $`Z_j`$ are independent copies. Then every acceptance effect obeys the finite-$`n`$ inequality

```math
b_n\geq e^{-nc}
       \left[\frac{a_n}{v_n}-u_n(c)\right]_+.
```

To prove it, compress $`T_n`$ to the null-support block. Pinching gives

```math
\mathrm{Tr}(\mathcal E_n(R_n)T_n)\geq a_n/v_n.
```

Let $`Q_n=\mathbf1\{\log W_n\leq nc\}`$. The operators $`Q_n`$, $`W_n`$, and $`\mathcal E_n(R_n)`$ commute. The contribution outside $`Q_n`$ is at most $`u_n(c)`$. On $`Q_n`$, the factor $`W_n^{-1}`$ is at least $`e^{-nc}`$. Since $`\eta_n`$ is a mixture of feasible alternatives,

```math
b_n\geq\mathrm{Tr}(\eta_nT_n)
\geq e^{-nc}\left[
  \mathrm{Tr}(\mathcal E_n(R_n)T_n)-u_n(c)
\right].
```

This proves the claim, with a positive part because probabilities are nonnegative.

For $`c=K+\delta`$ with $`\delta>0`$, Hoeffding's inequality gives

```math
u_n(K+\delta)\leq
\exp\!\left[-\frac{2n\delta^2}{(z_{\max}-z_{\min})^2}\right]
```

when the range is nonzero; if $`Z`$ is constant, this upper tail is zero. Thus any acceptance bounded below has Type-II exponent at most $`K`$. More generally, rearranging the same inequality gives

```math
a_n\leq v_n\left[
 e^{n(K+\delta)}b_n+u_n(K+\delta)
\right].
```

If $`\liminf_n[-\log b_n/n]>K`$, choose $`\delta`$ smaller than this exponent gap. Both terms then vanish exponentially apart from the polynomial factor $`v_n`$, and $`a_n\to0`$. This is the strong converse.

All constants are for the stated fixed instance. The formulas do not assert a uniform finite-sample bound while the dimension, effect spectrum, null spectral weights, or threshold vary with $`n`$.

## Matching spectral test

Measure $`\{P_i\}`$ separately on every copy and accept the null when the empirical frequency vector $`\widehat p_n`$ lies within $`\zeta`$ of $`p`$ in $`\ell_1`$ distance. A finite-confidence form is

```math
\alpha_n\leq2L\exp(-2n\zeta^2/L^2),\qquad
b_n\leq(n+1)^L\exp[-n\kappa(\zeta)],
```

where

```math
\kappa(\zeta)=
\inf_{\substack{x\in\Delta_L,\ \Vert x-p\Vert _1\leq\zeta\\q\in Q_r}}
      D(x\Vert q).
```

The first bound is a union of coordinate Hoeffding bounds; zero-weight coordinates are never observed under the null. The second is the method-of-types bound, uniform over all feasible alternative vectors. Compactness and lower semicontinuity imply $`\kappa(\zeta)\to K`$ as $`\zeta\downarrow0`$: minimizers have subsequences converging to $`(p,q)`$ with $`q\in Q_r`$, while $`x=p,q=q^*`$ supplies the reverse bound. Taking $`\zeta_n\downarrow0`$ slowly enough, for example $`\zeta_n=n^{-1/4}`$, proves achievability with vanishing Type-I error and hence at every fixed error threshold.

## Endpoint cases

| Condition | Certification conclusion |
| --- | --- |
| $`r\leq\mu`$ | The null is an allowed alternative. At error threshold $`\varepsilon`$, the optimal worst-case Type-II probability is exactly $`1-\varepsilon`$, attained by $`T_n=(1-\varepsilon)I`$; the exponent is zero. |
| $`\mu\lt r\lt f_{\max}`$ | The preceding theorem applies; $`0\lt K\lt\infty`$. |
| $`\mu\lt r=f_{\max}`$ | Every alternative is supported in the top eigenspace. For $`P_{\max}`$ its projector and $`p_{\max}=\mathrm{Tr}(\rho P_{\max})\lt1`$, the test $`T_n=I-P_{\max}^{\otimes n}`$ has Type-II error zero and Type-I error $`p_{\max}^n`$. Thus the fixed-error exponent is infinity. |
| $`r>f_{\max}`$ | The alternative set is empty; this is a vacuous testing problem, not a learning advantage. |
| $`F=cI`$ | The alternatives include the null when $`r\leq c`$ and are empty when $`r>c`$; there is no nontrivial threshold regime. |

At $`r=f_{\max}`$ with $`\mu\lt r`$, the finite-block divergence value is also infinity: the product spectral measurement has a positive-probability null outcome that has zero probability under every alternative. When $`r\leq\mu`$, the finite-block value is zero because the infimum includes $`\sigma=\rho`$.

The exact finite-block information value is proved in [Block measurements](block_measurements.md). The two feasible mixtures and their divergence identities are compared in [Modular mixtures](modular_mixtures.md). The [worked example](examples.md) makes the distinction from pairwise quantum distinguishability concrete.

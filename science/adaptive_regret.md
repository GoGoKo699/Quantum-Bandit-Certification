# Optimal regret with quantum memory

A learner can retain every specimen and measure them jointly before choosing its next arm. For a known common reward observable, this freedom leaves the optimal leading logarithmic regret equal to that of separate spectral measurements. The proof transfers the [fixed-sample certification bound](certification.md) to an adaptive bandit under pointwise consistency.

## Model and theorem

Fix a finite list of unknown states $`\rho_1,\ldots,\rho_A`$ on a finite-dimensional space. A classical request for arm $`i`$ returns one fresh copy of $`\rho_i`$. All supplied specimens are independent conditional on the fixed instance. The learner may retain a quantum register, apply arbitrary joint instruments to it, and use the resulting classical record and independent coins to select its next arm. The known reward effect is $`F=\sum_{\ell} f_{\ell}P_{\ell}`$, with $`0\leq F\leq I`$ and distinct spectral values $`f_{\ell}`$.

Write $`\mu_i=\operatorname{Tr}(\rho_i F)`$, $`\mu_*=\max_j\mu_j`$, $`\Delta_i=\mu_*-\mu_i`$, and let $`N_i(T)`$ count pulls of arm $`i`$ up to horizon $`T`$. The score is expected pseudo-regret $`R(T)=\sum_i \Delta_i\mathbb E N_i(T)`$. A policy is **pointwise consistent** when, on each fixed allowed instance, $`R(T)=o(T^{\alpha})`$ for every $`\alpha>0`$. Consistency is taken over all fixed state tuples in the model. In particular, it includes replacement of any one arm by a state that is strictly better than the other arms.

Suppose $`\mu_*<f_{\max}=\max_{\ell} f_{\ell}`$. For each suboptimal arm define $`p_{i\ell}=\operatorname{Tr}(\rho_iP_\ell)`$ and

```math
K_i=\min_{\substack{q\in\Delta_L\\ \sum_\ell f_\ell q_\ell\geq\mu_*}}
             D(p_i\Vert q),
\qquad
D(p_i\Vert q)=\sum_{\ell:p_{i\ell}>0}p_{i\ell}\ln\frac{p_{i\ell}}{q_\ell}.
```

Then $`0<K_i<\infty`$. For every consistent policy and every $`0<b<1/K_i`$, some $`c_b>0`$ satisfies

```math
\Pr\!\left[N_i(T)\leq\lfloor b\ln T\rfloor\right]=O(T^{-c_b}).
```

Consequently $`\liminf_{T\to\infty}\mathbb E N_i(T)/\ln T\geq1/K_i`$. Separate spectral measurements followed by empirical KL-UCB attain the matching upper limit for every suboptimal arm simultaneously. The optimal expected regret coefficient is

```math
\sum_{i:\Delta_i>0}\frac{\Delta_i}{K_i}.
```

For one anytime policy, the lower limit $`\liminf_{T\to\infty}N_i(T)/\ln T\geq1/K_i`$ also holds almost surely. The probability and expected-regret converse apply as well to a horizon-indexed sequence of policies with the stated pointwise consistency. The constants in the tail bound are instance- and policy-dependent. Each limit fixes the states, the effect and the arm set.

## 1. A cutoff event is a measurement on a fixed number of copies

Fix a suboptimal arm $`i`$ and the cutoff $`m=\lfloor b\ln T\rfloor`$. Consider the family of experiments that hold all other arms fixed and vary arm $`i`$ over a state $`\sigma`$. Supply $`m`$ copies from arm $`i`$ and $`T`$ copies from every other arm in separate queues. Run the policy through horizon $`T`$ with the same instruments, classical choices and coins. Reject immediately before the request for the $`(m+1)`$st copy of arm $`i`$ would be filled. Accept if the simulation reaches $`T`$ without that request.

The original policy decides whether to request that copy using only the already supplied systems and its classical record. Therefore the simulation's acceptance probability is exactly the original probability of $`N_i(T)\leq m`$, for every replacement $`\sigma`$. Any unused specimens can be discarded. The simulation is a binary quantum measurement with all other arms and the policy's initial workspace fixed. Absorbing those fixed systems into the measurement gives one effect $`0\leq E_{T,m}\leq I`$ on the $`m`$ arm-$`i`$ registers with

```math
a_{T,m}(\sigma)=\Pr_{\sigma}\!\left[N_i(T)\leq m\right]
=\operatorname{Tr}\!\left(E_{T,m}\sigma^{\otimes m}\right).
```

Here $`\Pr_\sigma`$ denotes probabilities on the instance with arm $`i`$ set to $`\sigma`$. The construction permits instruments acting jointly on copies from different arms. It depends on arm requests being classical and copies being generated independently.

## 2. A fixed finite family controls the alternatives

Put $`p=p_i`$ and $`\rho=\rho_i`$. Choose a threshold $`\mu_*<r<f_{\max}`$ sufficiently close to $`\mu_*`$ that $`bK(r)<1`$, where

```math
K(r)=\min_{\substack{q\in\Delta_L\\\sum_\ell f_\ell q_\ell\geq r}}D(p\Vert q).
```

Indeed $`K(r)\downarrow K_i`$ as $`r\downarrow\mu_*`$: mix a minimizing distribution at $`\mu_*`$ with a small weight of the top spectral point, and use continuity on the positive coordinates of $`p`$. Let $`q^*`$ attain $`K(r)`$, let $`S=\{\ell:p_\ell>0\}`$, and use the operators $`\Gamma=\sum_{\ell\in S}P_\ell`$, $`\Omega_S=\sum_{\ell\in S}(p_\ell/q_\ell^*)P_\ell`$ and $`\tau=\sum_{\ell\notin S}q_\ell^*P_\ell/\operatorname{rank}P_\ell`$ from the [support-complete certification construction](certification.md#classical-optimizer-and-null-support).

Use the independent phase rotations $`U_{\phi}=\sum_{\ell\in S}e^{i\phi_\ell}P_\ell`$ on the active space. The resulting alternative states are

```math
\sigma_{\phi}
  =U_{\phi}\Omega_S^{-1/2}\rho\Omega_S^{-1/2}U_{\phi}^{\dagger}
       \oplus\tau .
```

All phases preserve the spectral populations $`q^*`$, so all these states have mean reward at least $`r`$. In particular this construction allows zero null populations and rank-deficient states. Define $`\beta_{T,m}=\int a_{T,m}(\sigma_\phi)\,d\phi`$ using normalized Haar measure on the phase torus.

Pointwise consistency only bounds the regret on each fixed alternative. To control $`\beta_{T,m}`$, take a fixed $`0<\eta<1`$ and smooth the orbit with the maximally mixed state,

```math
\widetilde\sigma_{\phi}=(1-\eta)\sigma_{\phi}+\eta I/d.
```

Choose $`\eta`$ sufficiently small that all smoothed states have a common positive reward gap $`g`$ above $`\mu_*`$. Their eigenvalues are at least $`\eta/d`$. For any $`\xi>0`$, compactness gives finitely many representatives $`\widetilde\sigma_j`$ such that each $`\widetilde\sigma_\phi`$ is within $`(e^\xi-1)\eta/d`$ in operator norm of some representative. For that $`j`$,

```math
(1-\eta)\sigma_\phi\preceq\widetilde\sigma_\phi
       \preceq e^\xi\widetilde\sigma_j .
```

The right inequality uses the norm bound and $`\widetilde\sigma_j\succeq(\eta/d)I`$. The order is preserved by taking tensor powers of positive operators. Applied to a positive measurement effect, this gives

```math
\beta_{T,m}\leq
\exp\!\left(m\,[\xi-\ln(1-\eta)]\right)\max_j a_{T,m}(\widetilde\sigma_j).
```

Each representative defines a single IID replacement arm, and the finite set is fixed before $`T`$ grows. Under each replacement, the other arms have regret gap at least $`g`$. The expected pseudo-regret on that instance is $`R_j(T)`$, and the event $`N_i(T)\leq m`$ requires at least $`T-m`$ pulls of those other arms. Hence

```math
\max_j a_{T,m}(\widetilde\sigma_j)
\leq\frac{\max_j R_j(T)}{g(T-m)}
=o(T^{-1+\alpha})
```

for every $`\alpha>0`$. This finite-set step makes pointwise consistency sufficient.

## 3. The inherited pinching bound forces exploration

Write $`W_m=\Omega_S^{\otimes m}`$ on the active tensor space. Independent phase averaging pinches into occupation types with at most $`v_m=\binom{m+|S|-1}{|S|-1}`$ sectors. Denote this pinching by $`\mathcal P_m`$. The active block of the averaged alternative is $`W_m^{-1}\mathcal P_m(\rho^{\otimes m})`$, with positive outside blocks. The pinching commutes with $`W_m`$ and obeys $`\rho^{\otimes m}\preceq v_m\mathcal P_m(\rho^{\otimes m})`$.

With any fixed $`\zeta>0`$, the spectral region of $`W_m`$ where $`\ln W_m\leq m(K(r)+\zeta)`$ contributes at least $`e^{-m(K(r)+\zeta)}`$ times its accepted mass under $`\mathcal P_m(\rho^{\otimes m})`$. Its complement has probability at most $`u_m`$, the upper tail of the sum of $`m`$ independent copies of $`\ln(p_\ell/q_\ell^*)`$ drawn with probabilities $`p_\ell`$. That variable is bounded with mean $`K(r)`$. As in the [finite-confidence proof](certification.md#exact-finite-confidence-converse), the preceding observations yield

```math
a_{T,m}(\rho)\leq
v_m\left[e^{m(K(r)+\zeta)}\beta_{T,m}+u_m\right].
```

Here $`u_m`$ decays exponentially in $`m`$ by Hoeffding's inequality, or vanishes when all active log ratios coincide. The use of occupation types in place of the single modular parameter keeps the phase family compact. The same pinching bound applies since $`W_m`$ is scalar on each type.

Choose $`\zeta,\eta,\xi,\alpha>0`$ so small that

```math
b\,[K(r)+\zeta+\xi-\ln(1-\eta)]<1-\alpha ,
```

and keep these choices fixed. The two terms in the bound for $`a_{T,m}(\rho)`$ now decay as powers of $`T`$. The factor $`v_m`$ is polynomial in $`\ln T`$, and is absorbed by reducing the positive decay exponent. This proves the stated lower tail.

Multiplying the probability of $`N_i(T)>m`$ by $`m`$ bounds $`\mathbb E N_i(T)`$ from below. Sending $`T`$ to infinity and then $`b`$ up to $`1/K_i`$ gives the per-arm and regret converses. For an anytime policy take $`T_j=\lceil e^j\rceil`$. The lower-tail probabilities along this sequence are summable. Borel–Cantelli and monotonicity of $`N_i(T)`$ extend the lower limit between adjacent horizons, because $`\ln T_{j+1}/\ln T_j\to1`$. Take a countable sequence of cutoffs approaching $`1/K_i`$.

## 4. An attaining policy

Measure $`\{P_\ell\}`$ on each fresh copy and record the eigenvalue. These bounded finite-alphabet observations have mean $`\mu_i`$ on arm $`i`$. Initialize by pulling each arm once. At round $`t\geq3`$, let $`n_i`$ be the number of prior pulls of arm $`i`$ and let $`\widehat p_i`$ be its empirical distribution. Choose an arm with largest index

```math
\sup_{q\in\Delta_L}
\left\{\sum_\ell q_\ell f_\ell:
 n_iD(\widehat p_i\Vert q)\leq\ln t+\ln\ln t\right\}.
```

This is [empirical KL-UCB](https://doi.org/10.1214/13-AOS1119), applied to spectral outcomes as in [Ng](https://arxiv.org/abs/2609.40339). In the index optimization, any mass on a non-top outcome absent from the current sample may be moved to the top outcome. This leaves the divergence on the observed outcomes unchanged and can only increase the candidate mean. Thus the full-alphabet index agrees with the standard optimization over the empirical support and the known top outcome. Its upper bound is $`\limsup_T\mathbb E N_i(T)/\ln T\leq1/K_i`$ for each suboptimal arm. The classical proof compares each such arm against an optimal arm and permits ties among optimal arms. A positive affine rescaling of a nonconstant spectrum can put all rewards in $`[1/2,1]`$ if the chosen classical guarantee assumes strictly positive means. The rescaling keeps the feasible spectral distributions and $`K_i`$ unchanged.

The proof charges every pull. The attained result concerns the leading instance-dependent expected regret for classical arm requests and independent, fixed sources. Finite-horizon improvements and access through coherent reward queries are different questions. See [the two-arm qubit example](examples.md) and [prior work](../references/RELATED_WORK.md).

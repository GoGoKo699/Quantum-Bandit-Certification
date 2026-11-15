# Exact mixture divergences and their regularization

A mixture of IID alternatives can retain less distinguishability than any single IID alternative. For reward half-spaces, an explicit modular mixture evaluates this loss exactly for measured relative entropy at every copy number. A second, pinched mixture evaluates the regularized Umegaki relative entropy with an explicit finite-copy remainder. Both constructions include singular null states and zero spectral populations.

## Setting and inherited tools

Use the notation of [certification](certification.md). The known effect is $`F=\sum_i f_iP_i`$, the null is an arbitrary state $`\rho`$, $`p_i=\operatorname{Tr}(\rho P_i)`$, and $`\mu=\operatorname{Tr}(\rho F)\lt r\lt f_{\max}`$. Set

```math
\Lambda_r=\{\sigma:\operatorname{Tr}(\sigma F)\geq r\},\qquad
C_n=\operatorname{conv}\{\sigma^{\otimes n}:\sigma\in\Lambda_r\},
```

and let $`q^*`$ be any optimizer of

```math
K=\min_{q\in Q_r}D(p\Vert q),\qquad
Q_r=\{q\in\Delta_L:\textstyle\sum_iq_if_i\geq r\}.
```

The optimum is finite and positive; $`q_i^*>0`$ wherever $`p_i>0`$. All logarithms are natural. Define

```math
S=\{i:p_i>0\},\qquad
\Gamma=\sum_{i\in S}P_i,\qquad
\Omega_S=\sum_{i\in S}\frac{p_i}{q_i^*}P_i,\qquad
R_n=\rho^{\otimes n},\qquad W_n=\Omega_S^{\otimes n}.
```

Thus $`\rho=\Gamma\rho\Gamma`$ and $`\Omega_S`$ is strictly positive on $`\Gamma\mathcal H`$. Let $`v_n`$ count the distinct eigenvalues of $`W_n`$. For $`J`$ distinct eigenvalues of $`\Omega_S`$,

```math
v_n\leq\binom{n+J-1}{J-1}.
```

The measured relative entropy optimizes classical relative entropy over finite-outcome POVMs. We use the inherited variational identity of [Berta–Fawzi–Tomamichel, Lemma 1 and Theorem 2](https://arxiv.org/abs/1512.02615): for normalized states $`R`$ and $`Z`$,

```math
D_M(R\Vert Z)=
\sup_{X>0}\{\operatorname{Tr}(R\log X)+1-\operatorname{Tr}(ZX)\}.
```

The constant $`1`$ is fixed by $`\operatorname{Tr}R=1`$. The compression used below produces a subnormalized second operator, but does not change this constant. The existing general composite-IID regularization framework is due to [Berta–Brandão–Hirche](https://arxiv.org/abs/1709.07268); the contribution here is an explicit evaluation for the reward-half-space family, with finite-copy witnesses. The one-copy logarithmic-derivative witness is inherited from [Ng, Theorem 1](https://arxiv.org/abs/2609.40339).

## Exact finite-copy identity

For every $`n\geq1`$,

```math
\min_{Z\in C_n}D_M(R_n\Vert Z)=nK.
```

The minimum is attained by the normalized modular mixture constructed below. No positive population outside $`S`$ and no full matrix rank of $`\rho`$ is assumed.

### One common lower witness

Convex first-order optimality at $`q^*`$ gives, for every $`q\in Q_r`$,

```math
0\leq\left.\frac{d}{du}
D\bigl(p\Vert(1-u)q^*+uq\bigr)\right|_{u=0^+}
=-\sum_{i\in S}\frac{p_i}{q_i^*}(q_i-q_i^*).
```

Consequently,

```math
\sum_{i\in S}\frac{p_i}{q_i^*}q_i\leq1.
```

Extend $`\Omega_S`$ to the full Hilbert space by $`\Omega=\Omega_S\oplus0`$. Then

```math
\operatorname{Tr}(\sigma\Omega)\leq1\quad(\sigma\in\Lambda_r),
\qquad
\operatorname{Tr}(Z\Omega^{\otimes n})\leq1\quad(Z\in C_n).
```

For $`\epsilon>0`$, use the strictly positive trial operator

```math
X_\epsilon=
W_n\oplus\epsilon I_{(\Gamma^{\otimes n})^\perp}.
```

Because $`R_n`$ is supported on $`\Gamma^{\otimes n}`$,

```math
\operatorname{Tr}(R_n\log X_\epsilon)
=\operatorname{Tr}(R_n\log W_n)=nK.
```

The variational formula yields $`D_M(R_n\Vert Z)\geq nK-\epsilon`$. Letting $`\epsilon\downarrow0`$ proves the lower bound for every $`Z\in C_n`$. This argument avoids taking an inverse or logarithm of the zero block of $`\Omega`$.

### A normalized orbit when spectral populations vanish

Define the positive operators

```math
\chi=\Omega_S^{-1/2}\rho\Omega_S^{-1/2},\qquad
B=\sum_{i\notin S}q_i^*\frac{P_i}{\operatorname{rank}P_i}.
```

Their traces sum to one, although $`\chi`$ alone need not have trace one. The states

```math
\sigma_t=
\Omega_S^{-it/2}\chi\Omega_S^{it/2}\oplus B,
\qquad t\in\mathbb R,
```

are normalized and have spectral population vector exactly $`q^*`$. Hence every $`\sigma_t`$ is feasible. The fixed operator $`B`$ preserves the optimizer's probability mass outside the null support; discarding or renormalizing that mass would alter the claim.

Let

```math
\beta(t)=\frac{\pi}{2(\cosh(\pi t)+1)},\qquad
\zeta_n=\int_{\mathbb R}\beta(t)\sigma_t^{\otimes n}\,dt.
```

The logistic density integrates to one, so $`\zeta_n`$ is a normalized member of $`C_n`$. It is block diagonal with respect to $`\Gamma^{\otimes n}`$ and its complement. Its active block is

```math
A_n:=\Gamma^{\otimes n}\zeta_n\Gamma^{\otimes n}
=\int_{\mathbb R}\beta(t)
 W_n^{-(1+it)/2}R_nW_n^{-(1-it)/2}\,dt
=\mathcal L_{W_n}(R_n),
```

where $`\mathcal L_A`$ denotes the Fréchet derivative of the matrix logarithm:

```math
\mathcal L_A(Y)=\int_0^\infty(A+sI)^{-1}Y(A+sI)^{-1}\,ds.
```

For clarity, the equality of the two integral forms can be checked directly in an eigenbasis of $`A`$. The resolvent form has multiplier $`(\log a-\log b)/(a-b)`$, with its continuous value $`1/a`$ when $`a=b`$. The logistic form has the same multiplier because

```math
\int_{\mathbb R}\beta(t)e^{-itu}\,dt=\frac{u}{\sinh u},
\qquad u=\frac{\log a-\log b}{2}.
```

Thus the modular representation is valid also for singular $`Y\geq0`$; only $`A`$ is inverted, and here $`A=W_n>0`$ on the active space.

### Compression, stationarity, and the upper bound

Fix any full-space $`X>0`$ and write $`X_+=\Gamma^{\otimes n}X\Gamma^{\otimes n}`$ as an operator on the active space. Operator Jensen for the concave logarithm gives

```math
\Gamma^{\otimes n}(\log X)\Gamma^{\otimes n}\leq\log X_+.
```

The outside block of $`\zeta_n`$ is positive and the cross block vanishes. Therefore its contribution to $`-\operatorname{Tr}(\zeta_nX)`$ is nonpositive, and the full variational objective is bounded by

```math
g(X_+)=\operatorname{Tr}(R_n\log X_+)+1-
       \operatorname{Tr}(A_nX_+).
```

This is a concave differentiable function on positive definite active-space operators. The logarithmic derivative is self-adjoint for the Hilbert–Schmidt pairing, so

```math
\nabla g(W_n)=\mathcal L_{W_n}(R_n)-A_n=0.
```

Consequently $`W_n`$ is a global maximizer. Moreover $`\mathcal L_{W_n}(W_n)=I`$, and hence

```math
\operatorname{Tr}(A_nW_n)
=\operatorname{Tr}\bigl(R_n\mathcal L_{W_n}(W_n)\bigr)=1.
```

This trace equals one even when $`A_n`$ is subnormalized. It is not $`\operatorname{Tr}A_n`$. It follows that

```math
g(W_n)=nK+1-1=nK.
```

Every full-space variational objective is therefore at most $`nK`$. Conversely, the positive trials $`W_n\oplus\epsilon I`$ have objectives tending to $`nK`$ as $`\epsilon\downarrow0`$. We conclude

```math
D_M(R_n\Vert\zeta_n)=nK,
```

which, together with the common lower witness, proves the exact minimum over $`C_n`$.

## The Umegaki sandwich and its limit

For a separate feasible witness, let $`\eta_n`$ be the Cesaro average of the same orbit:

```math
\eta_n=\lim_{A\to\infty}\frac1A\int_0^A
             \sigma_t^{\otimes n}\,dt\in C_n.
```

Let $`\mathcal E_n`$ pinch into the eigenspaces of $`W_n`$. The active block of $`\eta_n`$ is

```math
\Gamma^{\otimes n}\eta_n\Gamma^{\otimes n}
=\mathcal E_n(\chi^{\otimes n})
=W_n^{-1}\mathcal E_n(R_n).
```

The other blocks are null-orthogonal. Pinching ensures $`\operatorname{supp}R_n\subseteq\operatorname{supp}\mathcal E_n(R_n)`$, and the two operators $`W_n`$ and $`\mathcal E_n(R_n)`$ commute. Thus, on the support entering the relative entropy,

```math
\log\eta_n=\log\mathcal E_n(R_n)-\log W_n.
```

It follows exactly that

```math
D(R_n\Vert\eta_n)
=nK+D\bigl(R_n\Vert\mathcal E_n(R_n)\bigr).
```

The pinching inequality $`R_n\leq v_n\mathcal E_n(R_n)`$ bounds the last term by $`\log v_n`$. Since $`D_M\leq D`$, the already proved measured-divergence lower bound applies to every feasible mixture. Therefore

```math
nK\leq\inf_{Z\in C_n}D(R_n\Vert Z)
\leq D(R_n\Vert\eta_n)
\leq nK+\log v_n.
```

For fixed input dimension and effect spectrum, $`\log v_n=O(\log(n+1))`$. The regularized value is consequently

```math
\lim_{n\to\infty}\frac1n
       \inf_{Z\in C_n}D(R_n\Vert Z)=K.
```

This evaluates the regularized mixture expression without treating an existence theorem as its evaluation. The strong testing converse and spectral achievability are proved directly in [certification](certification.md).

## What the mixture statement does and does not imply

The exact measured-divergence identity is an optimization over mixtures $`C_n`$. It does not equate divergence to a mixture with divergence to one of its components. In particular, one must not infer an upper bound on a finite-block max–min KL game by simply replacing its IID alternative with $`\zeta_n`$. The finite-block result uses the independent repetition argument in [Block measurements](block_measurements.md).

These fixed-copy mixture identities also do not by themselves prove an optimal regret coefficient for an unrestricted adaptive policy. Such a claim requires its own stopped-experiment and consistency argument. The charged input here is $`n`$ independently supplied specimens of one fixed state; neither coherent preparation access nor an inverse state-preparation oracle is used.

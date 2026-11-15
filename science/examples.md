# A complete qubit experiment

This example shows why distinguishability against a particular alternative is different from uniform certification against every state with a higher reward. The null has coherence in the reward basis, but the optimal leading certification rate is determined by its reward statistics alone.

## States and reward

Use the known projector reward and full-rank null

```math
F=|0\rangle\langle0|,
\qquad
\rho=\frac{I+0.9X}{2}
=\begin{pmatrix}1/2&9/20\\9/20&1/2\end{pmatrix},
\qquad r=\frac{19}{20}.
```

The null reward is $`p=\mathrm{Tr}(\rho F)=1/2`$. The alternative is any fixed qubit state $`\sigma`$ with $`\mathrm{Tr}(\sigma F)\ge19/20`$, supplied IID throughout the experiment. The tester knows the null; it is not asked to learn its Bloch direction from an uncharged training set.

Measuring $`F`$ on each copy produces a Bernoulli sample with success probability $`p=1/2`$ under the null and some $`q\ge19/20`$ under every alternative. With natural logarithms, the exact leading certification exponent is

```math
K=\mathrm{kl}\!\left(\frac12,\frac{19}{20}\right)
=\frac12\log\frac{100}{19}
=0.830365603410825\ldots .
```

The [certification theorem](certification.md) establishes this rate for arbitrary collective quantum tests when the type-I error tends to zero. The [fixed-block theorem](block_measurements.md) establishes the same per-copy max–min information value for every finite block size. Neither statement asserts equality of finite-copy error curves.

## A finite-confidence test

Let $`\widehat p_n`$ be the fraction of $`F`$-outcomes equal to one. Choose any threshold $`s`$ satisfying $`p\lt s\lt r`$, and accept the null exactly when $`\widehat p_n\le s`$. Standard binomial Chernoff bounds give

```math
\alpha_n\le \exp[-n\mathrm{kl}(s,p)],
\qquad
\beta_n^{\rm worst}\le \exp[-n\mathrm{kl}(s,r)].
```

Here $`\alpha_n`$ is the probability of rejecting the null when it is true. The second bound is uniform over all alternative states: their spectral success probabilities satisfy $`q\ge r`$, and the lower-tail probability decreases as $`q`$ increases. Coherence in $`\sigma`$ does not affect these outcome probabilities.

For specified targets $`\overline\alpha,\overline\beta\in(0,1)`$, the sufficient copy budget is therefore

```math
n\ge
\max\!\left\{
\frac{\log(1/\overline\alpha)}{\mathrm{kl}(s,p)},
\frac{\log(1/\overline\beta)}{\mathrm{kl}(s,r)}
\right\},
```

rounded up to an integer. This is an explicit achievable bound, not an optimal finite-sample formula.

For example, take $`s=4/5`$ and $`n=33`$. Accepting the null means observing at most $`26`$ successes. The Chernoff guarantees are

| Error | Guaranteed upper bound |
| --- | --- |
| Type I | $`e^{-33\mathrm{kl}(0.8,0.5)}<0.00173`$ |
| Worst-case type II | $`e^{-33\mathrm{kl}(0.8,0.95)}<0.00993`$ |

Thus both errors are below one percent using $`33`$ supplied copies, one qubit readout at a time, and one classical count. The guarantees are conservative. The exact risks of this particular test are the binomial tails

```math
\alpha_{33}
=2^{-33}\sum_{j=27}^{33}\binom{33}{j},
\qquad
\beta_{33}^{\rm worst}
=\sum_{j=0}^{26}\binom{33}{j}
\left(\frac{19}{20}\right)^j
\left(\frac1{20}\right)^{33-j}.
```

To approach the leading exponent $`K`$, use thresholds $`s_n=p+\delta_n`$ with $`\delta_n\downarrow0`$ and $`n\delta_n^2\to\infty`$, while keeping $`s_n\lt r`$. For instance, $`\delta_n=n^{-1/3}`$ works for all sufficiently large $`n`$. Hoeffding's bound makes the type-I error vanish, and continuity of $`\mathrm{kl}(s_n,r)`$ gives the type-II exponent $`K`$. The unrestricted converse proves that no collective test has a higher uniform exponent in this regime.

## The physical alternative orbit

The classical reverse-KL optimizer is $`q^*=(19/20,1/20)`$. Its positive tilt is

```math
\Omega=\begin{pmatrix}10/19&0\\0&10\end{pmatrix}.
```

The [modular-mixture construction](modular_mixtures.md) uses the genuine alternative states

```math
\sigma_t
=\Omega^{-(1+it)/2}\rho\Omega^{-(1-it)/2}
=\begin{pmatrix}
19/20 & (9\sqrt{19}/200)e^{it\log(19)/2}\\
(9\sqrt{19}/200)e^{-it\log(19)/2}&1/20
\end{pmatrix}.
```

Every member has reward exactly $`19/20`$. Its phase varies, while its diagonal populations and the magnitude of its coherence remain fixed. Positivity follows directly from the congruence construction. Explicitly, its determinant is $`361/40000>0`$.

One common phase $`t`$ is drawn for the entire block in the converse witness:

```math
\tau_n=\int_{-\infty}^{\infty}
\frac{\pi}{2(\cosh\pi t+1)}\,
\sigma_t^{\otimes n}\,dt.
```

This shared-parameter mixture is generally not $`\tau_1^{\otimes n}`$. That distinction makes it possible to obstruct one test that must work against all IID alternatives, while retaining the original single-copy alternative family. The witness obeys the exact identity

```math
D_{\rm M}(\rho^{\otimes n}\Vert \tau_n)=nK.
```

For orientation, its single-copy off-diagonal entry is

```math
(\tau_1)_{01}=\frac{19\log19}{400}
=0.139860851510406\ldots .
```

This is the one-copy logarithmic-derivative witness already developed by [Ng, §III](https://arxiv.org/html/2609.40339v1). The new many-copy step keeps the same modular phase across all copies rather than taking a product of that averaged state.

## Where the apparent collective advantage goes

For this same instance, [Ng, §§VI–VII](https://arxiv.org/html/2609.40339v1) reports the numerical value

```math
D_{\rm inf}
:=\inf_{\sigma:\mathrm{Tr}(\sigma F)\ge19/20}
D(\rho\Vert \sigma)
\simeq1.11733005>K.
```

This is a numerical comparison, not an exact closed-form evaluation used by the proof. The larger value means that every individual fixed alternative has a larger asymptotically accessible pairwise information distance after optimizing the quantum test for that alternative. It does not supply one measurement that works at that rate against the whole halfspace.

The collective certification rate remains $`K`$. The minimization over alternatives and optimization over measurements cannot be interchanged merely because pairwise quantum Stein testing is understood. The exact relation and the distinction from the pointwise measured-divergence envelope are in [block_measurements.md](block_measurements.md).

## Same reward populations, different coherence

Dephase the null in the reward basis:

```math
\rho_{\rm diag}
=\begin{pmatrix}1/2&0\\0&1/2\end{pmatrix}.
```

The coherent and diagonal nulls have the same reward populations, but different spectra. Their uniform certification exponents against the same reward threshold are identical:

| Null | Reward populations | Uniform certification exponent | Pointwise Umegaki halfspace distance |
| --- | --- | --- | --- |
| $`(I+0.9X)/2`$ | $`(1/2,1/2)`$ | $`K=\tfrac12\log(100/19)`$ | Numerically $`\simeq1.11733005`$ |
| $`I/2`$ | $`(1/2,1/2)`$ | $`K=\tfrac12\log(100/19)`$ | Exactly $`K`$ |

For the diagonal null, $`\mathrm{diag}(19/20,1/20)`$ attains the last-column value, and spectral data processing proves its optimality. Coherence changes the pairwise quantum distance while leaving the solved uniform certification rate unchanged. This comparison concerns the full alternative halfspace; restricting the alternatives to a smaller known model can change the conclusion.

The experiment needs no QRAM, inverse preparation, or coherent storage between copies. Its actual preparation, measurement, and classical-input costs are stated in [resources.md](resources.md). Pure-state and zero-population boundary cases are treated separately in [certification.md](certification.md).

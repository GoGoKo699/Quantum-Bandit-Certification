# Every fixed collective block has the spectral value

The [certification theorem](certification.md) concerns a binary decision on a growing number of copies. It also settles a different information game: choose any one measurement on a fixed block, then ask for its smallest KL divergence against all better-reward states.

Use the [model](model.md) with $`\mu\lt r\lt f_{\max}`$, an arbitrary reference state and fixed finite dimension. All outcomes in this chapter form a finite alphabet.

## The value and its lower bound

For any integer $`m\geq1`$,

```math
V_m=\sup_M\inf_{\sigma\in\Lambda_r}
\frac1mD\!\left(M(\rho^{\otimes m})\middle\Vert
                     M(\sigma^{\otimes m})\right)=K.
```

Measuring $`F`$ spectrally on each copy proves $`V_m\geq K`$. Under an alternative with spectral vector $`q`$, the full sequence of outcomes has distribution $`q^{\otimes m}`$. Additivity gives divergence $`mD(p\Vert q)`$, whose feasible minimum is $`mK`$.

## Why a better block would contradict certification

Fix a POVM $`M=\{M_x\}_{x=1}^{B}`$ on $`m`$ copies. Remove zero effects and put

```math
a_x=\mathrm{Tr}(M_x\rho^{\otimes m}),\qquad
b_x(\sigma)=\mathrm{Tr}(M_x\sigma^{\otimes m}),
\qquad
\mathcal B_M=\{b(\sigma):\sigma\in\Lambda_r\}.
```

The family $`\mathcal B_M`$ is compact. It contains a distribution positive on every remaining outcome: a full-rank feasible state exists because $`r\lt f_{\max}`$, and any nonzero positive effect has strictly positive expectation on its tensor power. Hence

```math
c_M=\inf_{b\in\mathcal B_M}D(a\Vert b)
```

is finite. The null distribution may have zero entries.

Repeat this same block measurement independently on $`\ell`$ blocks. For one fixed alternative, the resulting classical law is $`b(\sigma)^{\otimes\ell}`$; the null law is $`a^{\otimes\ell}`$. Accept the null when the empirical outcome vector is near $`a`$. The number of empirical types is at most $`(\ell+1)^B`$, and each type $`x`$ has probability at most $`\exp[-\ell D(x\Vert b)]`$ under any fixed $`b`$.

For a closed neighborhood of radius $`\zeta`$, compactness and lower semicontinuity imply

```math
\inf_{\substack{\Vert x-a\Vert _1\leq\zeta\\b\in\mathcal B_M}}
 D(x\Vert b)\longrightarrow c_M
\quad\text{as }\zeta\downarrow0.
```

Choose neighborhoods shrinking slowly enough that the null acceptance tends to one. This gives a uniform classical composite test at every rate below $`c_M`$ per block, without assuming $`\mathcal B_M`$ is convex.

If $`c_M>mK`$, choose a rate strictly between those values. The repeated measurement followed by this classical decision is a valid collective test on $`m\ell`$ quantum specimens with per-copy exponent greater than $`K`$. That contradicts the already-proved uniform certification converse. Therefore $`c_M\leq mK`$ for every fixed $`M`$, proving $`V_m\leq K`$.

The order matters: first fix $`m`$ and the block POVM, then let $`\ell`$ grow. This argument establishes every finite block, without relying on numerical searches over particular measurement bases.

## Two distinctions that protect the conclusion

The divergence to a mixture can be smaller than the divergence to every component. Consequently the [exact mixture identity](modular_mixtures.md) does not directly upper-bound this game by a Jensen or minimax swap. The repetition argument supplies the required bridge.

The theorem also does not determine the regret of every adaptive quantum-memory bandit policy. Such policies can change arm allocations, retain coherent memory between observations and stop at data-dependent times. Relating their expected copy count to a uniform fixed-sample certificate requires a separate argument; [Interpretation](interpretation.md) states that boundary explicitly.

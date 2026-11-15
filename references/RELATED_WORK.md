# Related work and attribution

The contribution is an explicit solution of reward-halfspace composite certification and its fixed-block measurement game. State discrimination, spectral measurements, classical type testing, operator pinching and modular logarithmic derivatives are established tools. Their use here should be separated from the new feasible many-copy witnesses and their operational consequences.

## Closest quantum-learning problem

[Siu Hin Ng, arXiv:2609.40339v1](https://arxiv.org/abs/2609.40339v1), *The Single-Copy Quantum Bandit Is Classical: An Exact Spectral Collapse* (2026), defines the states-as-arms reward model. Its Theorem 1 establishes the one-copy spectral collapse and a logarithmic-derivative least-favorable state. Section VI gives a Umegaki converse for arbitrary-memory regret and leaves the composite IID certification exponent and its adaptive-regret reduction open. Section VII defines the common-measurement block values separately from the pairwise min–max envelopes and reports two-copy numerical evidence.

The present work credits that one-copy result and model. It adds the exact all-copy uniform certification exponent, a strong converse, all-support mixture constructions and the equality of every fixed finite-block value. The unknown phase shared across all copies is the step that turns a one-copy witness into a feasible mixture of fixed IID alternatives. The unrestricted adaptive-regret optimum remains outside the result.

## Relative entropy and composite testing

[Mario Berta, Omar Fawzi and Marco Tomamichel, arXiv:1512.02615v2](https://arxiv.org/abs/1512.02615v2), *On Variational Expressions for Quantum Relative Entropies*, Letters in Mathematical Physics 107, 2239–2265 (2017), supplies the measured-relative-entropy variational formula. It also clarifies the distinction between measured and Umegaki relative entropy. The variational identity is inherited; the [exact mixture](../science/modular_mixtures.md) uses it on a newly specified feasible many-copy alternative.

[Mario Berta, Fernando G. S. L. Brandão and Christoph Hirche, arXiv:1709.07268v2](https://arxiv.org/abs/1709.07268v2), *On Composite Quantum Hypothesis Testing*, Communications in Mathematical Physics 385, 55–77 (2021), gives a general regularized relative-entropy formula for convex mixtures of IID hypotheses. This framework establishes how such regularized expressions enter testing; it does not itself evaluate the reward halfspace. Here the [pinched mixture](../science/modular_mixtures.md#the-umegaki-sandwich-and-its-limit) gives an explicit finite-copy upper bound and the matching single-letter limit. The testing strong converse is proved directly.

[Masahito Hayashi and Kun Fang, arXiv:2605.02203v2](https://arxiv.org/abs/2605.02203v2), *Operational interpretation of the reverse sandwiched Rényi divergences in composite quantum hypothesis testing* (2026), studies structured composite hypotheses and unknown phase orbits. Its explicit thermal-null example has a null invariant under the diagonal phase group. The present reference generally does not commute with the modular phase generator. That explicit example therefore does not directly give the reward-halfspace value. Phase averaging and composite testing are shared foundations, rather than claims of a new general twirling method.

## Classical statistics and operator foundations

[Cover and Thomas, *Elements of Information Theory*, second edition (2006)](https://www.wiley.com/en-us/Elements%2Bof%2BInformation%2BTheory%2C%2B2nd%2BEdition-p-9780471241959), Chapter 11, develops the method of types and classical hypothesis-testing exponents. These supply the spectral test and the uniform classical step in the fixed-block repetition proof. [Hoeffding's bounded-variable inequality](https://doi.org/10.1080/01621459.1963.10500830) supplies the finite-confidence concentration bounds. Neither classical ingredient is counted as new.

[Watrous, *The Theory of Quantum Information* (2018)](https://jhwatrous.github.io/books-and-courses.html) provides the underlying finite-dimensional measurement, entropy and channel framework. The pinching inequality and operator Jensen inequality are standard; the scientific account states the particular uses needed for this problem.

## Comparison boundaries

A theorem for a smaller statistical alternative family can exhibit a quantum advantage without contradicting the present result. The full reward halfspace, one common test, one fixed IID source and the order of limits are essential. Likewise an estimator's risk, a Haar-average source test and an unknown-state classifier are different operational objectives.

The comparison above concerns the stated primary sources and their inspected models. It is not an exhaustive priority certificate. Source versions are recorded in the [bibliography](references.bib); the analytical claims are proved in the [science account](../science/README.md).

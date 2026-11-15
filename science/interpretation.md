# Why the apparent collective advantage disappears

Collective quantum measurements can distinguish a known pair of noncommuting states more efficiently than separately measuring their copies. The present theorem asks a different operational question. A single test must reject every state whose reward exceeds a specified threshold. The identity of that alternative is not provided to the apparatus.

## A family can be harder than its individual members

The proof begins with the classical spectral distribution closest to the reference while meeting the better-reward constraint. Filtering the reference by the corresponding population ratios gives a family of states with exactly that distribution. Their coherences rotate under a modular phase, and every member remains a valid better-reward alternative.

For a fixed pair, the tester could use information in those coherences. A uniform certificate must work for all phases. Averaging one shared phase across the batch produces an alternative mixture that erases the leading usefulness of the reference coherence. A pinching step costs only a polynomial factor in the number of copies at fixed dimension, so it leaves the exponential confidence rate unchanged.

This is an information-theoretic converse. It allows arbitrary quantum storage, entangling gates, ancillas and a collective final binary measurement. The attaining protocol needs only independent spectral measurements of the reward, followed by a classical frequency test.

## What the source model permits

Each component of the witness is $`\sigma_t^{\otimes n}`$ for one fixed state. The shared phase is chosen once for the entire batch. The converse does not assume independently drifting copies, an adversary changing the source during measurement or an entangled physical source. The convex mixture is permitted in the lower-bound argument because binary acceptance probabilities are linear.

The worst-case alternative may depend on the sample budget. That is part of uniform certification. A pointwise statement for each fixed known alternative does not automatically survive the optimization over an entire unknown family.

## The learning conclusion and its boundary

The reward-halfspace experiment is the certification component of the states-as-arms quantum bandit model studied by [Ng](https://arxiv.org/abs/2609.40339v1). The result establishes that this certification component has no collective exponent advantage. It also establishes that every fixed finite measurement block has the same worst-case information value as separate reward readout.

These statements do not provide the optimal logarithmic regret coefficient of an unrestricted adaptive quantum-memory policy. In a bandit, the arm states are unknown, sampling times depend on previous outcomes, and retained quantum memory can influence later allocations. Pointwise consistency of a policy on every instance is not a uniform guarantee over a continuum of alternatives. An argument that averages such guarantees under a common prior needs its own proof.

Accordingly, a pairwise Umegaki regret lower bound should remain a lower bound. The certification theorem rules out attaining its larger information rate through a uniform fixed-sample certificate; it does not by itself prove that every adaptive learner must have the classical regret coefficient.

## Leading rates and practical costs

Equality of exponents permits different finite-copy errors and different constant or logarithmic corrections. The [finite-confidence inequalities](certification.md#exact-finite-confidence-converse) and the [33-copy qubit example](examples.md) state actual finite guarantees separately.

The theorem fixes dimension and all source parameters before taking the sample limit. A growing-dimensional family can change the polynomial pinching factor and the concentration constants. That requires a new joint-regime analysis. Hardware error rates, source latency and the gate cost of measuring a generic reward observable are also separate from a supplied-copy theorem; see [Resources](resources.md).

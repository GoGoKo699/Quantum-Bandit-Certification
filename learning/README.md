# Learn quantum bandit certification and regret

The tutorial starts with a 33-qubit certificate for a known reference against an unknown higher-reward source. It then uses that certification theorem to determine how often an adaptive learner must sample each suboptimal arm, even if the learner keeps the specimens for joint measurements.

| Reading goal | Start here |
| --- | --- |
| Follow the physical experiment through the proof's main ideas | [Worked tutorial](TUTORIAL.md) |
| Follow the adaptive regret proof directly | [Adaptive quantum-memory regret](../science/adaptive_regret.md) |
| Locate the project's full conceptual dependencies | [Thirty-milestone map](MILESTONES.md) |
| Connect the selected textbook to the actual proof | [Watrous bridge](WATROUS_BRIDGE.md) |
| Read exact statements and specialist proofs directly | [Scientific route](../science/README.md) |
| Reproduce the finite numerical checks | [Verification](../verification/README.md) |

The sole educational anchor is **John Watrous, *The Theory of Quantum Information* (2018), the author's standard-layout manuscript**, available through the [author's book page](https://jhwatrous.github.io/books-and-courses.html). The bridge selects the relevant sections; reading the entire book is not a prerequisite for the tutorial. Watrous uses base-two logarithms, while this project uses natural logarithms and rates in nats.

The map has **12 background milestones, M01–M12**, connecting specimens, measurements, errors, information, and pinching. Its **18 narrative milestones, M13–M30**, follow the shared-phase witnesses through fixed-sample certification, finite-block information, and adaptive regret. M28–M30 develop the pull-count test, the fixed finite family of alternative arms, and the optimal regret coefficient.

The certification experiment supplies the reference state as a classical description and charges each physical specimen. The bandit experiment supplies unknown arms and charges one fresh specimen per pull. Its optimal leading regret coefficient is attained by spectral reward readout followed by classical KL-UCB. Both asymptotic statements fix the instance first. The [model](../science/model.md), [resource account](../science/resources.md), and [interpretation](../science/interpretation.md) give the precise assumptions.

Textbook foundations, imported research tools, and the project's added proof steps have separate roles. The [bridge](WATROUS_BRIDGE.md#what-is-supplied-by-which-source) and [related-work account](../references/RELATED_WORK.md) identify them without adding another educational anchor.

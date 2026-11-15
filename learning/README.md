# Learn uniform quantum certification

The central question is whether keeping quantum specimens and measuring them together improves a certificate that must work against every higher-reward IID source. The simplest complete example uses 33 qubits, one reward measurement per qubit, and one classical count.

| Reading goal | Start here |
| --- | --- |
| Follow the physical experiment through the proof's main ideas | [Worked tutorial](TUTORIAL.md) |
| Locate the project's full conceptual dependencies | [Thirty-milestone map](MILESTONES.md) |
| Connect the selected textbook to the actual proof | [Watrous bridge](WATROUS_BRIDGE.md) |
| Read exact statements and specialist proofs directly | [Scientific route](../science/README.md) |
| Reproduce the finite numerical checks | [Verification](../verification/README.md) |

The sole educational anchor is **John Watrous, *The Theory of Quantum Information* (2018), the author's standard-layout manuscript**, available through the [author's book page](https://jhwatrous.github.io/books-and-courses.html). The bridge selects the relevant sections; reading the entire book is not a prerequisite for the tutorial. Watrous uses base-two logarithms, while this project uses natural logarithms and rates in nats.

The settled map has **12 background milestones, M01–M12**, connecting specimens, measurements, errors, information, and pinching into the known-reference task. Its **18 narrative milestones, M13–M30**, connect the qubit example to support completion, shared-phase witnesses, the strong converse, attaining spectral readout, and the finite-block consequence. Each milestone records its central question, understanding target, dependencies, conceptual connection, and source pointers.

Keep the scientific distinction visible throughout: this is certification of a supplied known reference against the full better-reward family. It is not tomography or a complete unknown-arm bandit learner. The theorem fixes the instance before the copy limit and determines leading confidence rates; the tutorial states finite-copy guarantees separately. The [model](../science/model.md), [resource account](../science/resources.md), and [interpretation](../science/interpretation.md) retain those boundaries.

Textbook foundations, imported research tools, and the project's added proof steps have separate roles. The [bridge](WATROUS_BRIDGE.md#what-is-supplied-by-which-source) and [related-work account](../references/RELATED_WORK.md) identify them without adding another educational anchor.

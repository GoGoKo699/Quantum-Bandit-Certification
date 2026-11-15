# Thirty milestones for uniform quantum certification

This is the project's common understanding map. Its 30 targets depend on the scientific contribution, with **12 background milestones** followed by **18 narrative milestones**. The background connects physical specimens and measurements to the statistical and operator framework. The narrative gives more space to the new shared-phase witnesses, their two different uses, and the operational conclusions. Both phases end with an integrated account.

The sole educational anchor is John Watrous, *The Theory of Quantum Information* (2018), using the author's standard-layout manuscript linked from the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). Chapter and section numbers below refer to that version. The book uses base-two logarithms; the project uses natural logarithms, so a book divergence is multiplied by $`\log 2`$ to express the same quantity in nats. Watrous supplies foundations; the project supplies the composite-family quantifiers, classical type-test estimates, logarithmic-derivative witness, and full certification argument where indicated. Primary research attribution is maintained in the [related-work account](../references/RELATED_WORK.md). The [anchor bridge](WATROUS_BRIDGE.md) explains the translation between the textbook and these project statements.

| Phase | IDs | Integrating endpoint |
| --- | --- | --- |
| Background and preliminaries | M01–M12 | A complete operational specification of the known-null uniform task |
| Narrative and contribution | M13–M30 | One connected explanation of the theorem, witnesses, consequences, and limits |

## Background and preliminaries

### M01 — A quantum specimen and its predictions

- **Central question:** What does a density operator specify about one supplied physical specimen?
- **Understanding target:** Explain positivity, unit trace, pure versus mixed states, and how a state predicts measurement outcomes; distinguish a specimen from its classical description.
- **Dependencies and story role:** Entry milestone. It establishes the object that the source supplies before any learning or certification claim is made.
- **Conceptual connection:** The theorem receives actual quantum copies even though the reference state is already classically known. These are different resources.
- **Source pointers:** Watrous, Chapter 2, §2.1 “Registers and states”; [model — supplied information](../science/model.md#supplied-information-and-hypotheses); [resources — what the tester receives](../science/resources.md#what-the-tester-receives).

### M02 — A reward effect and its spectral outcomes

- **Central question:** How can a known operator assign a mean reward while permitting several different readout records?
- **Understanding target:** Interpret an effect $`F`$, its spectral projectors $`P_i`$, and the probabilities $`p_i=\mathrm{Tr}(\rho P_i)`$. Distinguish the full spectral record from a Bernoulli outcome of $`\{F,I-F\}`$.
- **Dependencies and story role:** Uses M01. It connects one specimen to the project's physically specified reward and identifies the attaining measurement.
- **Conceptual connection:** Preserving the reward mean does not guarantee preserving all the information relevant to certification; the distinction matters for effects with more than two eigenvalues.
- **Source pointers:** Watrous, Chapter 1, §1.1 spectral linear algebra, and Chapter 2, §2.3 “Measurements”; [model — classical quantity](../science/model.md#the-classical-quantity); [resources — attaining acquisition](../science/resources.md#an-attaining-acquisition-scheme).

### M03 — Independent copies and collective measurements

- **Central question:** What extra operations become available when several quantum specimens are retained together?
- **Understanding target:** Read $`\rho^{\otimes n}`$ as independently prepared copies, explain the difference between separate and joint measurements, and keep source correlations distinct from correlations created during processing.
- **Dependencies and story role:** Uses M01–M02. It defines the potentially stronger competitor against which separate reward readout will be compared.
- **Conceptual connection:** The converse permits arbitrary collective processing of IID inputs. It does not assume that the physical source supplies an entangled batch.
- **Source pointers:** Watrous, Chapter 2, §§2.1–2.3 on composite registers, channels, and measurements; [model — supplied information](../science/model.md#supplied-information-and-hypotheses); [interpretation — source model](../science/interpretation.md#what-the-source-model-permits).

### M04 — Readout as a quantum-to-classical map

- **Central question:** How does a measurement turn a quantum experiment into an ordinary probability model?
- **Understanding target:** Identify the outcome distribution induced by a POVM and explain which information is discarded when only that classical record is retained.
- **Dependencies and story role:** Uses M02–M03. It connects the quantum apparatus to the classical statistics used for the attaining protocol and for the repeated-block argument.
- **Conceptual connection:** A quantum measurement may be complicated while its output is a finite classical alphabet. The proof uses this fact without treating arbitrary measurements as computationally cheap.
- **Source pointers:** Watrous, Chapter 2, §§2.2–2.3; [resources — attaining acquisition](../science/resources.md#an-attaining-acquisition-scheme); [block measurements — fixed outcome family](../science/block_measurements.md#why-a-better-block-would-contradict-certification).

### M05 — A binary certificate and its two errors

- **Central question:** What must a test guarantee when it accepts or rejects the reference state?
- **Understanding target:** Explain null acceptance, Type-I error, worst-case Type-II error, and why fixing a positive error tolerance differs from demanding exactly zero Type-I error.
- **Dependencies and story role:** Uses M01–M04. It supplies the performance criterion before introducing information distances.
- **Conceptual connection:** The output is one binary decision. An exponentially small error probability is not a reconstructed state, a learned model, or a selected best arm.
- **Source pointers:** Watrous, Chapter 3, §3.1 “Quantum state discrimination”; [model — exact certification theorem](../science/model.md#exact-certification-theorem); [certification — model and statement](../science/certification.md#model-and-statement).

### M06 — Relative entropy and the direction of comparison

- **Central question:** Why does the rate use $`D(p\Vert q)`$ with the null distribution first?
- **Understanding target:** Interpret classical relative entropy as a directional information quantity, use its zero-probability conventions and logarithm units, and distinguish an error exponent from an exact finite-copy risk.
- **Dependencies and story role:** Uses M04–M05. It introduces the classical rate whose role will be justified by matching tests and converses.
- **Conceptual connection:** The closest better-reward population vector minimizes reverse KL from the known null; reversing the arguments changes the optimization and its operational meaning.
- **Source pointers:** Watrous, Chapter 5, §§5.1.1–5.1.2 on classical entropic functions; [model — classical quantity](../science/model.md#the-classical-quantity); [examples — states and reward](../science/examples.md#states-and-reward).

### M07 — Pairwise quantum information and measured information

- **Central question:** What differs between quantum relative entropy and the information from one chosen measurement?
- **Understanding target:** Distinguish Umegaki relative entropy, measured relative entropy, and a fixed measurement's classical divergence; explain the data-processing comparison without assuming one measurement is optimal for every alternative.
- **Dependencies and story role:** Uses M03–M06. It prepares the apparent collective-information gap that motivates the project.
- **Conceptual connection:** A measurement optimized for a known pair need not certify an entire unknown family at that pairwise rate.
- **Source pointers:** Watrous, Chapter 3, §3.1, and Chapter 5, §§5.2.1–5.2.3; the research-level measured-divergence formula is supplied in [modular mixtures — inherited tools](../science/modular_mixtures.md#setting-and-inherited-tools); [examples — apparent advantage](../science/examples.md#where-the-apparent-collective-advantage-goes).

### M08 — Convex families and a common test

- **Central question:** What changes when one apparatus must handle every state satisfying a reward constraint?
- **Understanding target:** Explain a convex half-space of states, the order of the measurement and alternative optimizations, and why linear acceptance probabilities allow mixtures in a minimax converse.
- **Dependencies and story role:** Uses M01, M05, and M07. It turns a collection of pairwise problems into the actual uniform task.
- **Conceptual connection:** The alternative can depend on the test and copy number while remaining one fixed IID state within an experiment. Uniformity is an operational requirement, not a statement about drifting sources.
- **Source pointers:** Watrous, Chapter 1, §1.2 “Analysis, convexity, and probability theory,” and Chapter 2, §§2.1–2.3; project quantifiers in [model — supplied information](../science/model.md#supplied-information-and-hypotheses); [interpretation — source model](../science/interpretation.md#what-the-source-model-permits).

### M09 — Frequencies, concentration, and confidence rates

- **Central question:** How can many ordinary outcome records produce a reliable certificate?
- **Understanding target:** Connect empirical frequencies, a neighborhood of the null distribution, concentration of null outcomes, and a uniform exponential bound under alternatives; distinguish a sufficient copy budget from a finite-sample optimum.
- **Dependencies and story role:** Uses M04–M06 and M08. It supplies the classical mechanism that will attain the final rate and later repeat a fixed quantum block.
- **Conceptual connection:** A common test can be built from outcome counts, and its error bounds must control the whole alternative family.
- **Source pointers:** Watrous, Chapter 1, §1.2 and Chapter 5, §5.1 for probability and classical entropy foundations; the method-of-types and concentration steps are supplied in [certification — matching spectral test](../science/certification.md#matching-spectral-test) and [examples — finite confidence](../science/examples.md#a-finite-confidence-test).

### M10 — Positive filtering and functions of operators

- **Central question:** How can population ratios modify a quantum state without discarding its coherences?
- **Understanding target:** Explain spectral functional calculus, positive congruence filtering, the role of operator powers and logarithms, and why inverses must be restricted to a positive active subspace.
- **Dependencies and story role:** Uses M01–M02 and M06. It prepares the local construction of feasible alternatives rather than introducing the entire converse at once.
- **Conceptual connection:** The ratios between null and optimizer populations define a positive filter; support completion is needed when its active output is subnormalized.
- **Source pointers:** Watrous, Chapter 1, §1.1.3 on spectral functional calculus, and Chapter 2, §§2.1–2.2; [certification — null support](../science/certification.md#classical-optimizer-and-null-support); logarithmic-derivative details supplied in [modular mixtures — normalized orbit](../science/modular_mixtures.md#a-normalized-orbit-when-spectral-populations-vanish).

### M11 — Pinching and the cost of forgetting a phase

- **Central question:** What remains after coherence between selected eigenspaces is removed?
- **Understanding target:** Describe pinching as a channel that keeps diagonal blocks, relate phase averaging to those blocks, and explain why the number of tensor-power eigenspaces can grow only polynomially at fixed spectrum.
- **Dependencies and story role:** Uses M02–M03 and M10. It joins an operator operation to the asymptotic bookkeeping needed for the strong converse.
- **Conceptual connection:** Losing a polynomial factor in probability changes subleading terms but leaves a fixed positive exponential rate unchanged.
- **Source pointers:** Watrous, Chapter 4, §4.1.1, Definition 4.4 and Proposition 4.6 on pinching and mixed-unitary channels, with Chapter 1 spectral algebra; the project supplies the specific tensor-power counting argument in [certification — tensor-power mixture](../science/certification.md#a-feasible-mixture-on-every-tensor-power).

### M12 — The complete operational problem

- **Central question:** How do the physical inputs, error criterion, alternative family, and candidate rate fit into one experiment?
- **Understanding target:** State the known-null task coherently: classical descriptions of the reference and reward, actual IID specimens, one common binary test, the better-reward constraint, and the proposed rate $`K`$. Explain why neither pairwise discrimination nor bandit regret is the same task.
- **Dependencies and story role:** Integrates M01–M11 and closes the background phase at a global operational specification.
- **Conceptual connection:** The narrative can now investigate the actual contribution without changing its input promises, uniformity requirement, or charged output.
- **Source pointers:** Watrous, Chapters 2–3 and Chapter 5, §§5.1–5.2 as foundations; [model](../science/model.md); [interpretation](../science/interpretation.md); [resources](../science/resources.md).

## Narrative and contribution

### M13 — A coherent qubit with an apparently larger information rate

- **Central question:** Why might retaining coherent specimens seem useful in the project's concrete experiment?
- **Understanding target:** Explain the coherent qubit null, the projector reward, the higher-reward alternative cap, and the distinction between the spectral rate $`K`$ and the larger pointwise Umegaki distance reported for this instance.
- **Dependencies and story role:** Uses M12, especially M02 and M07. It starts the contribution with one complete physical setting whose apparent advantage the proof must resolve.
- **Conceptual connection:** Comparing the coherent and dephased nulls isolates information in coherence from the reward populations that control uniform certification.
- **Source pointers:** Watrous, Chapter 2, §§2.1–2.3; Chapter 3, §3.1; Chapter 5, §5.2; [examples — states and reward](../science/examples.md#states-and-reward), [apparent advantage](../science/examples.md#where-the-apparent-collective-advantage-goes), and [coherence comparison](../science/examples.md#same-reward-populations-different-coherence).

### M14 — The nearest feasible reward populations

- **Central question:** Which alternative population vector is closest to the null under the certification divergence?
- **Understanding target:** Define $`q^*`$ and $`K`$, explain existence, finiteness and positivity in the nontrivial threshold regime, and identify the first-order inequality satisfied by every feasible vector.
- **Dependencies and story role:** Uses M06, M08, and M13. It extracts the classical object from which both quantum witnesses will be built.
- **Conceptual connection:** Convex optimality supplies one common operator witness; the construction does not begin by choosing a different quantum measurement for each alternative.
- **Source pointers:** Watrous, Chapter 1, §1.2 and Chapter 5, §5.1; [certification — optimizer](../science/certification.md#classical-optimizer-and-null-support); [modular mixtures — common lower witness](../science/modular_mixtures.md#one-common-lower-witness).

### M15 — Completing missing support without renormalizing it

- **Central question:** How can a feasible optimizer use an eigenspace that the null never occupies?
- **Understanding target:** Explain the active set $`S`$, its projector $`\Gamma`$, the positive active tilt $`\Omega_S`$, the subnormalized filtered state, and the added orthogonal completion carrying the remaining optimizer mass.
- **Dependencies and story role:** Uses M10 and M14. It resolves a load-bearing boundary case before the witness is tensorized.
- **Conceptual connection:** Positivity shows the null has no cross terms into a zero-population eigenspace. Keeping the missing mass makes every completed alternative normalized and feasible, including for pure nulls.
- **Source pointers:** Watrous, Chapter 1, §1.1 and Chapter 2, §2.1; [certification — null support](../science/certification.md#classical-optimizer-and-null-support); [modular mixtures — normalized orbit](../science/modular_mixtures.md#a-normalized-orbit-when-spectral-populations-vanish).

### M16 — A whole orbit of genuine better-reward states

- **Central question:** What can vary in an alternative while its reward populations remain fixed at $`q^*`$?
- **Understanding target:** Describe the modular phase rotation of the filtered active state, explain positivity and normalization after completion, and show conceptually why all orbit members remain feasible.
- **Dependencies and story role:** Uses M14–M15. It turns a classical optimizer into the quantum family that obstructs a common certificate.
- **Conceptual connection:** The unknown phase is relevant to pairwise coherent discrimination, while the reward constraint cannot reveal it.
- **Source pointers:** Watrous, Chapter 1 spectral operator powers and Chapter 2, §§2.1–2.2; [examples — physical orbit](../science/examples.md#the-physical-alternative-orbit); [modular mixtures — normalized orbit](../science/modular_mixtures.md#a-normalized-orbit-when-spectral-populations-vanish).

### M17 — One shared phase across the entire batch

- **Central question:** Why does averaging $`\sigma_t^{\otimes n}`$ differ from taking a tensor power of an averaged state?
- **Understanding target:** Explain a prior over one fixed IID source choice, the convex hull $`C_n`$, and why a shared-parameter mixture is a valid converse witness without changing the original physical source promise.
- **Dependencies and story role:** Uses M03, M08, and M16. It connects the local orbit to the full batch while preserving the model's quantifiers.
- **Conceptual connection:** Binary acceptance is linear in the density operator. This permits a mixture in a lower bound even though a component source remains IID throughout an experiment.
- **Source pointers:** Watrous, Chapter 1, §1.2 and Chapter 2, §§2.1–2.3; [model — source promises](../science/model.md#supplied-information-and-hypotheses); [interpretation — source model](../science/interpretation.md#what-the-source-model-permits); [examples — shared-phase mixture](../science/examples.md#the-physical-alternative-orbit).

### M18 — The logistic mixture and the logarithmic derivative

- **Central question:** Why is one particular phase distribution useful for an exact information identity?
- **Understanding target:** Relate the logistic modular average to the Fréchet derivative of the operator logarithm, distinguish the full normalized mixture from its active block, and recognize that the derivative identity is a supplied analytical ingredient.
- **Dependencies and story role:** Uses M10 and M15–M17. It identifies the first witness's local algebraic mechanism.
- **Conceptual connection:** The same shared phase on every copy turns the one-copy logarithmic-derivative witness into a tensor-power construction.
- **Source pointers:** Watrous, Chapter 1, §1.1 and Chapter 5, §5.2 for operator and relative-entropy foundations; the new use of the research-level derivative representation is derived in [modular mixtures — normalized orbit](../science/modular_mixtures.md#a-normalized-orbit-when-spectral-populations-vanish).

### M19 — A lower bound that holds for every mixture

- **Central question:** How does classical optimality become one common measured-divergence witness?
- **Understanding target:** Explain how the first-order condition gives $`\mathrm{Tr}(\sigma\Omega)\leq1`$ for all alternatives, how this tensorizes to every mixture in $`C_n`$, and why a positive trial limit handles the zero outside block.
- **Dependencies and story role:** Uses M07, M14–M15, and M17. It supplies the universal lower side of the exact finite-copy identity.
- **Conceptual connection:** The variational witness is shared across the whole feasible family, just as the operational test must be.
- **Source pointers:** Watrous, Chapter 1, §1.2 and Chapter 5, §5.2; the Berta–Fawzi–Tomamichel formula and its application are supplied in [modular mixtures — inherited tools](../science/modular_mixtures.md#setting-and-inherited-tools) and [common lower witness](../science/modular_mixtures.md#one-common-lower-witness).

### M20 — The exact measured-divergence collapse

- **Central question:** Why does the logistic mixture attain the common lower value exactly at every copy number?
- **Understanding target:** Connect compression Jensen, the nonpositive contribution of outside blocks, concavity, and stationarity at $`W_n`$. Explain why $`\mathrm{Tr}(A_nW_n)=1`$ even when the active block is subnormalized, yielding $`\min_{C_n}D_M=nK`$.
- **Dependencies and story role:** Integrates M15 and M18–M19. It closes the first complete proof mechanism before moving to the different witness used for the strong converse.
- **Conceptual connection:** Exact finite-copy measured divergence is achieved by a normalized mixture, not by silently normalizing its active block or swapping a mixture with one component.
- **Source pointers:** Watrous, Chapter 1 operator analysis and Chapter 5, §5.2; the specific operator Jensen and variational argument is supplied in [modular mixtures — compression and stationarity](../science/modular_mixtures.md#compression-stationarity-and-the-upper-bound).

### M21 — A second mixture obtained by pinching

- **Central question:** Why introduce a Cesaro average when the logistic witness already has an exact identity?
- **Understanding target:** Explain how long-time averaging of the same feasible orbit pinches tensor-power eigenspaces and produces the active block $`W_n^{-1}\mathcal E_n(R_n)`$; distinguish this witness's purpose from the logistic mixture's purpose.
- **Dependencies and story role:** Uses M11, M15–M17, and M20. It opens the direct strong-converse proof with a witness whose population factors can be bounded.
- **Conceptual connection:** The two averages share a physical family but solve different analytical tasks; confusing them obscures which operator comparison is valid.
- **Source pointers:** Watrous, Chapter 4, §§4.1–4.2; [certification — feasible tensor-power mixture](../science/certification.md#a-feasible-mixture-on-every-tensor-power); [modular mixtures — Umegaki sandwich](../science/modular_mixtures.md#the-umegaki-sandwich-and-its-limit).

### M22 — Polynomial sectors and a classical likelihood sum

- **Central question:** Why does the pinching penalty disappear from the leading confidence rate?
- **Understanding target:** Explain the bound on the number of distinct tensor-power eigenvalues, read $`\log W_n`$ as a sum of independent spectral log-ratios under the null, and connect its mean to $`K`$.
- **Dependencies and story role:** Uses M09, M11, M14, and M21. It joins the quantum block comparison to classical concentration.
- **Conceptual connection:** A polynomial sector count and an exponentially small likelihood tail operate on different scales; fixing the instance before taking the sample limit is essential.
- **Source pointers:** Watrous, Chapter 1, §§1.1–1.2 and Chapter 5, §5.1; project counting and concentration in [certification — tensor-power mixture](../science/certification.md#a-feasible-mixture-on-every-tensor-power) and [finite-confidence converse](../science/certification.md#exact-finite-confidence-converse).

### M23 — The fixed-error strong converse

- **Central question:** What fails if a common collective test tries to exceed the spectral confidence exponent?
- **Understanding target:** Explain the finite-confidence lower bound on worst-case Type-II probability, its consequence at every fixed positive Type-I tolerance, and the stronger conclusion that null acceptance tends to zero above rate $`K`$.
- **Dependencies and story role:** Integrates M05, M08, and M21–M22. It completes the unrestricted converse rather than inferring a strong statement from a weak relative-entropy bound alone.
- **Conceptual connection:** The conclusion allows arbitrary coherent memory and a collective measurement, yet concerns uniform fixed-sample certification of a known null.
- **Source pointers:** Watrous, Chapter 3, §3.1 and Chapter 5, §§5.1–5.2 as foundations; the project-specific strong-converse proof is in [certification — exact finite-confidence converse](../science/certification.md#exact-finite-confidence-converse); [model — exact theorem](../science/model.md#exact-certification-theorem).

### M24 — A spectral certificate that reaches the bound

- **Central question:** How does a simple acquisition scheme match an unrestricted quantum converse?
- **Understanding target:** Explain the empirical-frequency acceptance region, the two error bounds, the shrinking-neighborhood limit, and the explicit 33-copy qubit guarantee; distinguish a conservative finite budget from the exact asymptotic exponent.
- **Dependencies and story role:** Uses M02, M09, M13, and M23. It closes the operational theorem by pairing the lower limit with an actual attaining test.
- **Conceptual connection:** Independent spectral measurements preserve exactly the classical information needed for uniform certification, while classical counts suffice between specimens.
- **Source pointers:** Watrous, Chapter 2, §2.3 and Chapter 5, §5.1; [certification — matching spectral test](../science/certification.md#matching-spectral-test); [examples — finite confidence](../science/examples.md#a-finite-confidence-test); [resources — acquisition scheme](../science/resources.md#an-attaining-acquisition-scheme).

### M25 — Evaluating the regularized quantum expression

- **Central question:** How can a many-copy quantum relative-entropy optimization have the same leading classical value?
- **Understanding target:** Connect the exact measured-divergence lower bound to the pinched mixture's Umegaki identity and the logarithmic pinching remainder; explain why the sandwich evaluates the regularized limit rather than merely citing its existence.
- **Dependencies and story role:** Uses M07, M20–M22, and M24. It integrates the two witness mechanisms into the composite-information interpretation.
- **Conceptual connection:** The expression optimized over IID mixtures differs from the pointwise Umegaki distance to one alternative, which may remain strictly larger.
- **Source pointers:** Watrous, Chapter 5, §§5.2.1–5.2.3 and Chapter 4 for the entropy and channel foundations; the finite-copy sandwich and inherited composite framework are in [modular mixtures — Umegaki sandwich](../science/modular_mixtures.md#the-umegaki-sandwich-and-its-limit); [examples — apparent advantage](../science/examples.md#where-the-apparent-collective-advantage-goes).

### M26 — Why every fixed collective block has the same value

- **Central question:** How would one apparently better finite block produce an impossible full certificate?
- **Understanding target:** Fix a block and its finite-outcome POVM, repeat it independently, and explain how the resulting compact classical family would violate certification if its per-copy worst-case KL value exceeded $`K`$. Keep fixed-block value, pointwise envelope, and optimization order distinct.
- **Dependencies and story role:** Uses M04, M08–M09, M23–M25. It transfers the established certification result to a separate operational information game.
- **Conceptual connection:** Repetition supplies the missing bridge. A direct inference from divergence to a mixture to divergence to one component would be invalid.
- **Source pointers:** Watrous, Chapter 2, §2.3, Chapter 1, §1.2, and Chapter 5, §5.1; [block measurements](../science/block_measurements.md); [model — exact finite-block value](../science/model.md#exact-finite-block-information-value).

### M27 — Null support, threshold endpoints, and exact zero error

- **Central question:** Which changes of regime are covered by the theorem, and which change the testing problem itself?
- **Understanding target:** Explain why pure and zero-population nulls remain covered in the nontrivial regime, why a feasible null gives exponent zero, why a strict top-eigenspace threshold gives infinite exponent, and why empty alternatives or exact zero Type-I error need separate treatment.
- **Dependencies and story role:** Uses M05, M15, and M23–M26. It tests the theorem's conceptual coverage against all load-bearing boundaries rather than treating singular states as a silent exception.
- **Conceptual connection:** Rank, threshold position, and the error convention affect different parts of the model; they must not be conflated into one generic “boundary case.”
- **Source pointers:** Watrous, Chapter 2, §2.1, Chapter 3, §3.1, and Chapter 5 support conventions; [certification — endpoint cases](../science/certification.md#endpoint-cases); [model — exact certification theorem](../science/model.md#exact-certification-theorem); [modular mixtures — support completion](../science/modular_mixtures.md#a-normalized-orbit-when-spectral-populations-vanish).

### M28 — What the statistical equality costs to implement

- **Central question:** What resources are paid by the attaining protocol and by its collective competitors?
- **Understanding target:** Account for supplied copies, known classical descriptions, one incoming quantum register, outcome counts, spectral readout, classical processing, and the binary output. Explain why a generic dense reward may be expensive to measure and why fixed hardware error need not preserve an exponential confidence rate.
- **Dependencies and story role:** Uses M01–M04, M24, and M27. It joins the theorem's statistical conclusion to the actual physical acquisition scheme.
- **Conceptual connection:** Equality of supplied-copy exponents does not establish equal runtime, energy, finite-copy errors, or hardware advantage; no QRAM or preparation inverse is hidden in the attaining test.
- **Source pointers:** Watrous, Chapter 2, §§2.1–2.3 for operational foundations; the project-specific accounting and precision estimate are in [resources](../science/resources.md); [examples — finite confidence](../science/examples.md#a-finite-confidence-test).

### M29 — The learning consequence and the remaining adaptive question

- **Central question:** What does this certification result change about the proposed value of collective quantum examples?
- **Understanding target:** Explain the established absence of a collective uniform certification exponent advantage and the exact finite-block consequence, while preserving the separate unknown-state, stopping-time, and pointwise-consistency issues of unrestricted adaptive bandit regret. Identify inherited one-copy results and the new many-copy evaluation.
- **Dependencies and story role:** Uses M12–M13 and M23–M28. It connects the proved mechanism to its scientific significance without converting an unresolved adaptive reduction into a result.
- **Conceptual connection:** Pairwise information can be present yet unavailable to one common certificate over a full alternative family. Reducing that family, changing the input promise, or asking an adaptive question requires its own analysis.
- **Source pointers:** Watrous, Chapter 3, §3.1 and Chapter 5, §5.2 as foundations; [interpretation — learning conclusion](../science/interpretation.md#the-learning-conclusion-and-its-boundary); [block measurements — distinctions](../science/block_measurements.md#two-distinctions-that-protect-the-conclusion); [related work](../references/RELATED_WORK.md).

### M30 — One integrated account of the contribution

- **Central question:** How do the task, two witnesses, matched protocol, and learning limits form one scientific story?
- **Understanding target:** Explain the whole chain: a known coherent null and one unknown better-reward IID source; the reverse-KL optimizer; support completion and a feasible shared-phase orbit; exact measured divergence from the logistic mixture; pinching and a fixed-error strong converse; spectral attainment; the Umegaki sandwich; finite-block repetition; endpoints, resources, and the unresolved adaptive-regret boundary.
- **Dependencies and story role:** Integrates all earlier milestones and closes the narrative phase. The target is the connected contribution and its scope, not every technical lemma in the repository.
- **Conceptual connection:** The same alternative family makes each witness legitimate, the two witnesses have different analytical roles, and the matching spectral test turns the converse into an exact operational conclusion.
- **Source pointers:** Watrous, Chapters 1–5 only to the extent used in M01–M29; [scientific reading route](../science/README.md), [model](../science/model.md), [certification](../science/certification.md), [modular mixtures](../science/modular_mixtures.md), [block measurements](../science/block_measurements.md), [examples](../science/examples.md), [interpretation](../science/interpretation.md), and [resources](../science/resources.md).

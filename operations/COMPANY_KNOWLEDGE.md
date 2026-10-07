# Company knowledge and learning

Use this method at task intake, when discussing a decision or owner observation, and at the end of a work cycle. Company entries and guides select authoritative operational documents. The optional memory binding selects reusable knowledge. Keep both outside this package.

## Consult knowledge at task intake

1. Resolve the company through [local company discovery](LOCAL_COMPANIES.md). Read the entry and applicable guides, project decisions, and research before planning or dispatching work.
2. If the registration or entry supplies `memory_binding_path`, resolve it from the entry directory. When both supply it, they must resolve to the same file. Verify the binding's server/workspace against the selected company. An absent binding means memory is not configured. An unreadable or conflicting binding stops memory access and company writes until routing is repaired; never substitute another instance.
3. Invoke `/multica-team:team-memory` with that binding, the task, and the actual member/project IDs. The [team memory skill](../skills/team-memory/SKILL.md) and [specification](../SPEC.md) are the canonical memory contract in this same package. In a runtime without slash commands, read those files and preserve their supporting references. If the package is unavailable to a worker, report the lookup gap and continue only work that does not depend on it.
4. Cite relevant entries and their sources in the plan or handoff, explaining applicability to this task. Record an empty lookup or unavailable evidence honestly. Recheck changing facts against current sources. Carry the binding pointer and member/project scope in authorized worker instructions and task handoffs, using paths reachable by that runtime. Console installation alone does not wire workers.

Consulting knowledge grants no capture, attachment, scheduling, or permission changes. Explicit saves and candidate handoffs use the installed memory skill. If memory is not configured, offer `/multica-team:setup` as an optional step rather than creating an instance during an ordinary task.

## Decisions and grill-with-doc

For each decision, read the existing decision record and the document that defines the outcome. Create or update a document under the company's configured operations root as `decisions/<date>-<topic>.md` with a stable decision ID, using [the decision template](templates/DECISIONS-template.md). Link it from `DECISIONS.md` in that operations root when the draft starts, recording its ID and initial status. Append status transitions to the log so unresolved and declined decisions remain discoverable. Scale the document to the choice; a small decision can be a short record.

Grill-with-doc means testing that draft against the owner's intent and available evidence. Identify the most consequential unresolved assumption. Ask only questions that could change the choice, success predicate, or scope. Put each answer, source, disagreement, and remaining unknown into the draft so the next discussion starts from the document. Distinguish an owner's desired outcome from an inferred explanation. Compare alternatives, including keeping the current approach, and state what evidence would reverse the choice.

End with a decision or an explicitly unresolved question, a named decision owner, and a validation plan. Append the accepted outcome to the company decision log and update affected editable documents in the same authorized task. Changes to locked rules, acceptance criteria, instructions, access, or spend remain proposals under existing company governance. A memory entry may link to the decision's reusable rationale; it does not replace the operational record.

## Owner observations

Treat an owner observation as input for investigation, not as proof of a general rule. Record it in company operations using the observation section of the decision template. Keep these fields distinct:

| Field | Record |
|---|---|
| Intent | The outcome the owner wants, in their words |
| Evidence | The observed behavior, source, date, and scope; include counterexamples or gaps |
| Hypothesis | A possible explanation, labeled unverified until supported |
| Mechanism | How that explanation could produce the observed result |
| Intervention | The smallest proposed change, its owner, and existing authorization boundary |
| Validation | A baseline, observable success/failure signal, review point, and result or pending status |

Label intent as explicit or inferred and cite its source. Continue read-only investigation and already authorized work without interrupting the owner. Ask about missing intent only when the ambiguity would change the action, scope, success predicate, or authorization; otherwise record the assumption and its uncertainty. Run only authorized interventions. Append validation results and revise the hypothesis when evidence disagrees. Raw observations, temporary experiment state, and pending approvals stay in operations. After validation, a reusable lesson can be proposed to memory with its evidence and limitations.

## End-of-cycle retrospective

At a completed task, release, or measurement checkpoint, review a bounded set of supplied task results, review findings, decisions, owner observations, and validation evidence. Use existing evidence; additional paid runs or experiments need their own authorization.

Record a short retrospective in company operations with the input references, outcomes against intended success, unknowns, and proposed interventions. Propose only reusable memory candidates supported by those inputs. For each proposal, state the claim, intended member/project/team scope, evidence, uncertainty, related existing knowledge, and why it would help a future task. No candidates is a valid result.

Return proposals for an explicit save or acceptance decision. When candidate writing is authorized, hand them to `/multica-team:team-memory` with the resolved binding; its rules govern capability, concurrency, and shared acceptance. Existing-memory consolidation is a separate `/multica-team:dreaming` invocation with the bounded inputs. A retrospective does not automatically capture memory, promote shared knowledge, change company rules, or enable a recurring job. Plugin defects go through `/multica-team:feedback`; company method proposals remain in company operations.

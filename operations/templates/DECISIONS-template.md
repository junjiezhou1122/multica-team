# Decisions — what we tried, what we rejected, and why

**Append-only.** Add entries; never rewrite or delete one. This file exists so a rejected
idea stays rejected instead of returning every quarter — the issue threads hold the same
history, but re-reading them costs more than anyone will pay.

**What belongs here:** an approach that was proposed and turned down, a tool evaluated and
passed over, a design taken and later reversed, an experiment that failed. **What doesn't:**
current state (that's the spec, roadmap and guide) or a deferral with a revisit trigger
(that's `_ops/LATER.md`).

---

## {{YYYY-MM-DD}} — {{the decision, in one line}}

**Considered:** {{option A · option B · option C}}
**Chose:** {{what}} · **Rejected:** {{what}}
**Because:** {{the evidence — a measurement, a quote from the docs, a cost, a constraint.
"It felt cleaner" is not evidence.}}
**Would revisit if:** {{the condition that would make this wrong — a price change, a
version, scale. Omit only if genuinely permanent.}}
**Decided by:** {{who}} · **Where:** {{issue link}}

## Decision draft and grill-with-doc

Use before acceptance for a consequential choice. Follow the installed Team Ops company knowledge method. Keep unresolved drafts separate from accepted append-only entries.

- Decision ID: {{stable ID}}; document: {{_ops/decisions/<date>-<topic>.md}}
- Index entry: {{link and initial status in _ops/DECISIONS.md; append transitions}}
- Original statement: {{owner's exact words and source}}
- Intended outcome: {{explicit or inferred intent, provenance, observable success}}
- Configuration context: {{current authoritative configuration; historical configuration at observation time, source/date or unknown}}
- Current evidence: {{sources, dates, scope, counterexamples, unknowns}}
- Alternatives: {{options, including keeping the current approach}}
- Open questions: {{questions that could change the choice; answers and sources}}
- Validation plan: {{baseline, success/failure signal, owner, review point}}
- Status: {{proposed, unresolved, accepted, or declined; decision owner}}

## Owner observation investigation

Keep this record in company operations. Add only the validated reusable lesson to a separately authorized memory proposal.

- Intent: {{the outcome the owner wants}}
- Evidence: {{observation, provenance, date, scope, and gaps}}
- Hypothesis: {{possible explanation and confidence}}
- Mechanism: {{how it could cause the observed result}}
- Intervention: {{smallest change, owner, and authorization status}}
- Validation: {{baseline, success/failure signal, review point, result or pending}}

Append follow-up results with their sources. Keep earlier observations and failed hypotheses attributable.

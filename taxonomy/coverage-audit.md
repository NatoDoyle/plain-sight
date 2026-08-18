---
id: coverage-audit
type: meta
name: Coverage Audit
aliases: [gap analysis, kb health, completeness audit, final audit, what's missing]
status: complete
last-updated: 2026-07-01
---

# Coverage Audit

> The knowledge base's honest self-assessment at completion: what it covers, how healthy the graph is, where the evidence is thin, and **what it deliberately does not do**. A defense KB that claimed completeness would be violating its own first principle. This audit records the real numbers (from `tools/kb.py`), the intentional gaps, and the limitations the [[defense-agent-spec|defense agent]] must carry forward.

## Final inventory

**166 files, all `status: complete`, 0 validation errors, 0 warnings.** By type:

| Type | Count | |
|---|---|---|
| mechanism | 23 | the psychological levers (why it works) |
| tactic | 68 | observable moves (what they do) |
| dynamic | 10 | multi-tactic temporal systems |
| context | 12 | arena dossiers (where it happens) |
| profile | 6 | actor patterns (who) |
| vulnerability | 9 | target-side risk factors |
| defense | 15 | counters, exit, recovery |
| meta | 8 | foundations + synthesis |

This matches the ROADMAP backlog (166/166 checked). Tiers 0–7 complete, plus a 2026-07-01 maintenance/QA pass (Tier 8: `emergent-insights`, `tone-policing`, `spiritual-abuse`, `overton-window-shifting`) and **Tier 9 — Cognitive Bias Codex integration (2026-08-18)**: 14 clustered mechanism files, 6 extended files, 13 pointer aliases, and `bias-codex-index` mapping all 189 listed codex entries (188 unique) to a graded home.

**Tier 9 open items** (logged per-file in `sources/bibliographies/`, none load-bearing). A verification pass on 2026-08-18 closed 4 of 24 open spot-checks outright and materially strengthened the two that mattered most: **Winters & Jeglic 2017** — which anchors the "No grooming detection signal" fence in `fluency-familiarity` — and **Bond et al. 2022** — which anchors the "fading affect is reduced, not reversed, in PTSD" rider in the `memory-self-editing` Safety notes — are both now confirmed verbatim against primary abstracts. `fluency-familiarity` and `time-distortions` have zero open gates. **20 gates remain**, each flagged in its own bibliography against the specific claim it supports; none carries a load-bearing body claim without an in-line hedge, and most now require a paywalled PDF rather than another index (Meissner & Brigham's odds ratios, the JPSP transparency/spotlight integers, Ritov & Baron's ~10x threshold, Buehler's Study 1 figures). One item is a live correction rather than a gap: **Haslam & Levy 2006**'s abstract undercuts the widely repeated split-direction pattern (immutability → lower prejudice, entitativity → higher) — the authors report all three dimensions predicting prejudice. The KB asserts nothing on this point and the log is marked *unsupported-pending-body-check* so the split is not restored from memory by a future session.

## Graph health

- **1,318 directed edges** (symmetric relations expanded both ways) across 11 of the 12 typed relations (`variant-of` is defined but currently unused), compiled into `graph/edges.yaml`; the tactic⇄mechanism and tactic⇄context matrices regenerate cleanly.
- **Edge distribution:** `distinguished-from` 402 · `appears-in` 228 · `countered-by` 212 · `exploits` 196 · `co-occurs-with` 192 · `composed-of` 36 · `targets` 21 · `favored-by` 16 · `escalates-to` 7 · `enables` 5 · `precedes` 3.
- **The large `distinguished-from` count is deliberate** — it is the false-positive immune system: every tactic is tied to its innocent look-alike, backed by **79 contrast concepts** registered in the glossary (`taxonomy/glossary.md`).
- **Orphan nodes: 7, all `meta`, by design** — [[master-taxonomy]], [[epistemic-guardrails]], [[felt-sense-index]], [[playbooks-compendium]], [[defense-agent-spec]], [[coverage-audit]], and [[emergent-insights]] carry no *typed* edges because they are navigational/foundational; they connect through wikilinks, not the tactic graph. (The eighth meta file, [[manipulation-vs-influence]], is fully connected via `distinguished-from`.) Every mechanism, tactic, dynamic, context, profile, vulnerability, and defense is connected.

**Thin layers (acknowledged):** the **causal/temporal edges are sparse** — `enables` (5), `precedes` (3), `escalates-to` (7), and `variant-of` (0 — defined but unused). Co-occurrence and exploitation are richly mapped; *sequence* is mostly captured prose-side in the dynamics and [[playbooks-compendium]] rather than as edges. A future pass could promote more of those sequence claims to typed `precedes`/`escalates-to` edges.

## Evidence honesty

145 of 151 files carry an `evidence:` grade (the 6 ungraded are foundational `meta`):

- **established 29 · supported 89 · clinical 14 · contested 7 · folk 6.**
- The **7 contested** and **6 folk** constructs are flagged inline wherever load-bearing — e.g., "brainwashing/mind-control" as an irresistible mechanism (APA rejected DIMPAC), "Stockholm syndrome," post-traumatic-growth specifics, *Body Keeps the Score* neurobiology, ego-depletion. Nothing folk is laundered as fact.
- Disputed figures were corrected during review (e.g., separation-homicide rate scoped to Campbell's ~44%, not the folk "75%"; MLM "99.6% lose money" attributed to Taylor, not the FTC). The KB errs toward under-claiming precision.

## Safety coverage

**53 files carry a `safety:` flag**, each with a `## Safety notes` section and crisis resources, spanning DV escalation, self-harm threats, stalking, child grooming, elder exploitation, spiritual/religious abuse, and cult exit. Crisis numbers (988; National DV Hotline 1-800-799-7233; Childhelp 1-800-422-4453; DOJ Elder Fraud 833-372-8311; FTC; FBI IC3; UK Refuge) were verified digit-by-digit in review and are consolidated in the [[defense-agent-spec]] escalation table. Since the 2026-07-01 pass the validator enforces the flag and the `## Safety notes` section **each require the other** (bidirectional), closing the false-negative gap that had left two stalking/DV files unflagged.

## Retrieval spot-test (and its honest finding)

Three realistic scenarios were grep-tested against the KB:

- *"New partner checks my phone and calls me paranoid"* → keyword grep surfaced [[financial-abuse]] and related but **not** the best matches ([[stalkerware-monitoring]], [[coercive-control]], [[gaslighting]]) at the top.
- *"Online crypto romance asks me to deposit"* → correctly surfaced [[romance-scam-arc]], [[con-anatomy]], [[ai-enabled-manipulation]] — plus one false hit ([[fud-competitor-tactics]], on the word "doubt").
- *"Boss praises me publicly but takes credit and sets impossible deadlines"* → noisy; single-keyword grep returned weak matches.

**Finding:** raw single-keyword grep is **noisy and insufficient** on its own. This is precisely why the Tier-7 retrieval layer exists: the [[felt-sense-index]] (felt experience → candidates), the typed **graph** (co-occurrence/exploitation expansion), and the [[defense-agent-spec]]'s mandated *read-the-Caveats* step are the disambiguating path. **The agent must retrieve via felt-sense + graph, not bare keyword search.**

## Deliberate gaps & limitations

The KB is complete *to its scope* — not omniscient. Carried-forward limitations:

1. **Jurisdictional bias.** Legal/crisis resources are **US-centric** (UK partial). The legal "is this actionable?" layer assumes US/UK frames; everywhere else needs localization.
2. **Cultural variation is under-developed.** Norms for directness, family obligation, hierarchy, and gift-giving vary; the KB flags this ([[epistemic-guardrails]]) but does not yet have culture-specific dossiers. Risk of importing one culture's "red flags" as universal.
3. **Recognition-oriented, not clinical.** This grounds *recognition and defense*; it is **not** a diagnostic manual, treatment guide, legal advice, or substitute for professionals. It labels behaviors, never people.
4. **Phenomenology is `folk`-graded.** Survivor-language and forum patterns inform recognition vocabulary only, and are marked as such.
5. **Sparse causal edges** (above) — sequence lives in prose more than in edges.
6. **Living document.** New tactics emerge (AI-enabled manipulation is already a moving target); the backlog is append-only and the KB needs periodic `needs-update` review.

## Recommendations (future work)

- Localize safety/legal resources beyond US/UK; add culture-variation notes to the context dossiers.
- Promote prose sequence-claims into typed `precedes`/`escalates-to` edges to thicken the causal layer.
- Periodic refresh of the fast-moving files ([[ai-enabled-manipulation]], [[dark-patterns-social-urgency]], [[disinformation-playbooks]]).
- Build the agent against [[defense-agent-spec]] and run the evaluation scenarios there; feed misses back as new edges/caveats.

## Conclusion

The knowledge base meets its specification: **151 topics across 8 tiers, fully cross-linked, evidence-graded, safety-flagged, and false-positive-guarded**, validating with zero errors. Its defining features are the ones a naive version would lack — a 79-concept false-positive layer, 53 safety-escalating files, honest grading of contested constructs, and a retrieval design ([[felt-sense-index]] + graph + mandatory caveats) that resists over-detection. It is ready to ground the [[defense-agent-spec|defense agent]]. The gaps above are real and recorded, not hidden — which is the only honest way to finish a knowledge base about deception.

## Sources

Self-generated from the repository at completion using `python3 tools/kb.py validate / graph / matrix / stats` (file counts, edge counts and distribution, evidence-grade tallies, safety-flag inventory) and direct grep retrieval tests, originally run 2026-06-30 and refreshed 2026-07-01 after the maintenance/QA pass (Tier 8 additions + audit fixes). No external claims; this file audits the KB against its own ROADMAP and the methodology in `METHODOLOGY.md`.

## See also

[[master-taxonomy]] · [[defense-agent-spec]] · [[felt-sense-index]] · [[playbooks-compendium]] · [[epistemic-guardrails]] · [[manipulation-vs-influence]]

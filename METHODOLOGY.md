# METHODOLOGY.md — how topics get researched and written

The knowledge base is built **one topic at a time**, each researched to saturation before its file is marked complete. Research mode is **hybrid**: draft from the established literature, then targeted web sweeps to verify claims, attach citations, capture recent developments, and import skeptical critiques.

## The 7-step pipeline (per topic)

1. **Scope note.** Define the topic's boundaries (what's in, what belongs to neighboring files), 3–6 key questions the file must answer, and expected edges to existing/planned files. Keep it in the working session, not committed.
2. **Source sweep.** Launch 3–5 parallel research subagents, split by source category (see `sources/SOURCES.md`):
   - academic/empirical (peer-reviewed studies, meta-analyses)
   - practitioner/clinical books and frameworks
   - regulatory/NGO data (FTC, FBI IC3, charity research, court records)
   - phenomenology (survivor forums, memoirs — recognition language only)
   - skeptic/critique (replication status, concept-creep, contrarian takes)
   Each agent returns structured findings with full citations, URLs, short quotes for load-bearing claims, and a confidence tag. Log the merged source list to `sources/bibliographies/<id>.md`.
3. **Synthesize.** Write `<folder>/<id>.md` from `templates/template-<type>.md`. Grade evidence per the rubric below; cite load-bearing claims inline `[n]`; wikilink first mentions of KB concepts.
4. **Red-team review.** One adversarial subagent reviews the draft against the checklist below and returns prioritized issues.
5. **Revise** until the review passes.
6. **Link & index.** Declare typed edges (single-declaration rule, see `CLAUDE.md`); add glossary entries for new terms; register new aliases (each alias lives on exactly one file — `kb.py validate` warns on duplicates); tick the topic in `ROADMAP.md` and set `status: complete`; append any newly discovered topics to ROADMAP as `backlog`; run `kb.py validate`, `graph`, `matrix`; commit `Add <id> (<type>)`.
7. **Saturation check** (the definition of "all sources exhausted"): every applicable source category swept; additional searching yields no materially new claims (marginal novelty ≈ 0); all scope-note questions answered or explicitly marked open in the file's Evidence & debates section; red-team passed.

## Evidence grading rubric

| Grade | Bar | Calibration examples |
|---|---|---|
| `established` | Replicated findings / meta-analytic support / converging methods | Reciprocity effects; anchoring; misinformation effect on memory |
| `supported` | Peer-reviewed empirical support + clinical consensus, limited replication breadth | DARVO (Freyd lab studies); abusive-supervision outcomes; dark-pattern prevalence |
| `clinical` | Practitioner literature, case series, professional consensus; thin formal study | Many coercive-control micro-tactics; hoovering; FOG dynamics |
| `folk` | Popular construct with face validity but no validated research base — useful vocabulary, flagged as such | "Narcissistic supply"; "flying monkeys"; "future faking" |
| `contested` | Active scholarly dispute or known-weak construct | Stockholm syndrome; parental alienation *syndrome*; micro-expression lie detection |

Rules: a file's `evidence:` field reflects its *core construct*; weaker sub-claims get flagged inline ("evidence: folk" parenthetical or an Evidence & debates note). Never silently mix grades. When a folk construct names something real but unvalidated, keep the name (it's what users search) and say plainly what is and isn't known.

## Source standards

- Prefer primary and meta-analytic sources; quote operative definitions exactly.
- Offense playbooks (sales manuals, *48 Laws of Power*, PUA material) are read **defensively**: catalog the move, its tells, and its counter — never reproduce operational scripts beyond what recognition requires.
- Survivor forums and memoirs inform **Recognition** sections (markers, typical phrases, felt-sense) and are graded anecdotal; they never carry causal or prevalence claims.
- Legal claims carry jurisdiction labels and statute/case cites.
- Note paywalls; prefer accessible mirrors (author pages, PMC, SSRN) when available.
- Every file ends with a numbered source list; the per-topic bibliography in `sources/bibliographies/` keeps the fuller sweep log including sources consulted but not cited.

## Red-team review checklist

1. Any claim without support (citation or clearly-labeled clinical/folk grade)?
2. Any misattributed/garbled citation? (Spot-check 2–3 against the web.)
3. Caveats & false positives: would a reasonable innocent behavior trigger this file's Recognition section? Are innocent explanations, base rates, and concept-creep warnings adequate?
4. Missing major perspective (cultural variation, neurodivergence, gender symmetry/asymmetry debates, skeptical literature)?
5. Distinguishability: does the file clearly separate itself from its nearest neighbors (`distinguished-from` edges + text)?
6. Safety: does content touching DV/self-harm/stalking carry the `safety:` flag, a Safety notes section, and crisis resources?
7. Defensive orientation: could any section read as a how-to? Rewrite to recognition/counter framing.
8. Retrieval quality: stable headings, concrete phrases in Recognition, wikilinks present, edges declared?

## Checkpoints (every ~8–10 completed topics)

- Regenerate `graph/edges.yaml` + matrices; review for orphan nodes (files with <2 inbound/outbound edges) and missing obvious links.
- Terminology-consistency pass (same concept, same term, one id; new aliases added).
- Update README status line and ROADMAP stats.
- **Retrieval spot-test:** run `python3 tools/kb.py eval` (Layer A — deterministic: every retrieval doorway is registered and named in the skill, every mechanism/tactic/dynamic is reachable from one, every stored scenario's expectations resolve, and no `Must-not-surface` id is reachable from its declared entry path). Scenarios live in `meta/agent-evals.md`; add one for any new concept family, and the tier gate will refuse a new `## Tier N` until you do.
  Periodically also run **Layer B** — the blind two-session behavioural protocol in that file, which samples what Layer A cannot check: escalation ordering, calibration, refusal quality, diagnosis creep. Log failures as ROADMAP fixes and, where the failure is a retrieval gap, as a new `Regression-for:`-tagged scenario.
- Commit `Checkpoint: <n> topics`.

## Session workflow

A working session = scaffold maintenance (if needed) + 1–5 topics through the full pipeline, sequentially. The repo carries all process state (ROADMAP statuses + this file); any future session resumes via the protocol in `CLAUDE.md` with zero conversational memory required.

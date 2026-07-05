# CLAUDE.md — AI operating manual for the Plain Sight knowledge base

This repo is a defensive knowledge base on manipulation, built to ground a future defense agent. You (the AI session) are both its librarian and its researcher. This file tells you how to query it, extend it, and never corrupt it.

**Consultation vs authoring:** when a user brings a *real situation* (possible manipulation, abuse, or a scam), invoke the `defense-agent` skill — `.claude/skills/defense-agent/SKILL.md` operationalizes `meta/defense-agent-spec.md` (safety gate first, retrieval order, calibration, output contract). The rest of this file is for authoring and maintaining the KB.

## Prime directives

1. **Defensive orientation.** Every entry exists so targets can recognize and counter manipulation. Lead with recognition and counters. Never reframe content as advice for manipulating people.
2. **Caveats are first-class.** Every tactic/dynamic file MUST have a real **Caveats & false positives** section (innocent explanations, base rates, concept-creep warnings). A KB that over-detects is as harmful as one that under-detects. See `meta/epistemic-guardrails.md`.
3. **Evidence honesty.** Grade every file (`evidence:` field) and flag contested constructs inline. Never launder folk psychology into established fact. When literatures disagree, say so.
4. **Safety escalation.** Files touching domestic violence, self-harm threats, or stalking carry a `safety:` flag and a Safety notes section with crisis resources. The future agent must escalate, not just analyze.
5. **Label behaviors, not people.** The KB describes patterns of behavior. It never provides grounds to diagnose a real individual with a disorder.
6. **One concept, one file, one id.** Don't create near-duplicate entries; extend or link instead.

## Resume protocol (start every working session here)

1. Read `ROADMAP.md` → find the next unchecked topic (respect tier order unless told otherwise).
2. Re-read `METHODOLOGY.md` (the 7-step pipeline) and the relevant `templates/template-<type>.md`.
3. Run `python3 tools/kb.py stats` to confirm the repo state matches ROADMAP.
4. Execute the pipeline for ONE topic at a time: scope → parallel source sweep → synthesize → red-team review → revise → link & index → validate.
5. Update the topic's checkbox + status, run `python3 tools/kb.py validate && python3 tools/kb.py graph && python3 tools/kb.py matrix`, commit (one commit per topic: `Add <id> (<type>)`).
6. Every ~8–10 topics: synthesis checkpoint (see METHODOLOGY.md §Checkpoints).

## Schema

### Frontmatter (constrained YAML — flat keys, scalars and lists of plain strings only, no inline comments, no nested maps)

```yaml
---
id: gaslighting                # REQUIRED. kebab-case, == filename stem, globally unique
type: tactic                   # REQUIRED. mechanism|tactic|dynamic|context|profile|vulnerability|defense|meta
name: Gaslighting              # REQUIRED. Display name
aliases: [crazy-making]        # optional. Search synonyms; must not collide with other ids/aliases
domains: [intimate-relationships, workplace-bosses]   # edge → appears-in (targets context ids)
exploits: [memory-fallibility, certainty-needs]       # edge: tactic → mechanism
co-occurs-with: [isolation-tactics, darvo]            # edge: symmetric correlation
precedes: []                   # edge: temporal sequence (this usually comes before X)
escalates-to: [coercive-control]                      # edge: causal intensification
enables: []                    # edge: makes X possible/easier
countered-by: [documentation-practices]               # edge: → defense ids
distinguished-from: [memory-divergence]               # edge: disambiguation (id, alias, or glossary contrast concept)
variant-of: []                 # edge: → parent tactic
favored-by: [narcissistic-patterns]                   # edge: tactic → profile
targets: [people-pleasing-fawn]                       # edge: tactic → vulnerability
composed-of: []                # edge: dynamic → constituent tactics (dynamics only)
severity: high                 # low|medium|high|critical (typical harm potential)
evidence: supported            # REQUIRED for tactic/mechanism/dynamic/profile/vulnerability/defense;
                               #   optional for context/meta (include when the file makes graded claims).
                               #   established|supported|clinical|folk|contested (rubric in METHODOLOGY.md)
safety: dv-escalation          # optional flag: file contains crisis-escalation guidance
status: complete               # REQUIRED. backlog|researching|drafted|reviewed|complete|needs-update
last-updated: 2026-06-09       # REQUIRED. YYYY-MM-DD
---
```

Omit edge fields that are empty rather than leaving `[]` (templates show all fields; delete unused ones).

### Edge semantics (12 relations)

| Field | Reads as | From → To |
|---|---|---|
| `exploits` | pulls this psychological lever | tactic/dynamic → mechanism |
| `domains` | appears in this arena (`appears-in`) | tactic/dynamic/profile → context |
| `co-occurs-with` | found together (correlation, symmetric) | tactic ↔ tactic |
| `precedes` | typically happens before | tactic/dynamic → tactic/dynamic |
| `escalates-to` | intensifies into (causal) | tactic → tactic/dynamic |
| `enables` | makes possible/easier (causal) | tactic → tactic/dynamic |
| `countered-by` | is countered by | tactic/mechanism/dynamic → defense |
| `distinguished-from` | innocent/neighboring look-alike (symmetric) | any → any or contrast concept |
| `variant-of` | specialized form of | tactic → tactic |
| `favored-by` | characteristic of this actor pattern | tactic → profile |
| `targets` | preferentially aimed at | tactic/dynamic → vulnerability |
| `composed-of` | built from these moves | dynamic → tactics |

**Single-declaration rule:** declare each edge in exactly ONE file — the file where it is most salient (usually the more specific one). `kb.py graph` compiles the full bidirectional union into `graph/edges.yaml`; never hand-mirror edges in both files.

**Edge targets** must be: an existing file id, an alias, an id listed in `ROADMAP.md` (pending topics are fine), or a contrast concept registered under `## Contrast concepts` in `taxonomy/glossary.md`. `kb.py validate` enforces this.

### Body structure

Use the section order from `templates/template-<type>.md`. Non-negotiable sections for tactics: **Recognition** (markers · typical phrases · felt-sense indicators · escalation signs), **Counter-strategies**, **Caveats & false positives**, **Sources**. Cite load-bearing claims inline as `[1]` against the numbered Sources list. Wikilink the first mention of any KB concept: `[[gaslighting]]` or `[[gaslighting|piped text]]`.

## Query cookbook

```bash
# Everything that co-occurs with a tactic (declared direction)
rg -l "co-occurs-with:.*gaslighting" --glob '*.md'
# Both directions + all relations for one concept: use the compiled graph
rg "gaslighting" graph/edges.yaml
# All tactics in a context
rg -l "domains:.*workplace-bosses" tactics/
# All files countered by a given defense
rg "countered-by:.*documentation-practices" -l
# Find by alias or phrase ("crazy-making", "you're too sensitive")
rg -il "crazy-making|too sensitive"
# All contested-evidence files (treat claims cautiously)
rg -l "evidence: contested|evidence: folk"
# Status dashboard
python3 tools/kb.py stats
```

For semantic questions ("partner checks my phone and calls me paranoid — what is this?"), grep candidate phrases across `tactics/` Recognition sections, then follow `graph/edges.yaml` for co-occurring tactics, then ALWAYS read the Caveats sections of whatever you found before answering.

## Toolchain

```bash
python3 tools/kb.py validate   # schema, enums, id=filename, dangling edges/wikilinks. Run before every commit.
python3 tools/kb.py graph      # regenerate graph/edges.yaml
python3 tools/kb.py matrix     # regenerate graph/tactic-mechanism.md + graph/tactic-context.md
python3 tools/kb.py stats      # coverage by type/status, roadmap cross-check
```

All stdlib; no installs needed. Frontmatter must stay within the constrained subset (flat, no nesting, no inline comments) or the parser will reject it.

## Style

- Plain English, no fluff. Write for a smart stressed-out person at 2am and for an AI retrieving snippets.
- Concrete > abstract: real phrases ("If you loved me you would…"), observable behaviors, named patterns.
- Short sections with stable headings (retrieval anchors). Bold the term being defined.
- Severity language proportional to evidence. "May indicate", not "proves".
- US/UK legal points are jurisdiction-labeled; the KB is not legal advice.

## Do not

- Do not write "how to manipulate" framings, scripts for executing tactics, or optimization advice for influence campaigns.
- Do not diagnose real, named individuals; do not present trait labels as certainties.
- Do not add a tactic file without Caveats & false positives — it will fail review.
- Do not hand-edit `graph/edges.yaml`, `graph/tactic-mechanism.md`, `graph/tactic-context.md` (generated).
- Do not introduce new frontmatter fields, types, statuses, or edge relations without updating this file, `kb.py`, and `METHODOLOGY.md` together.

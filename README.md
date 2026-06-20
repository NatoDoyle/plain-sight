# Mind Protector

A defensive knowledge base on manipulation: every major tactic, the psychological mechanisms it exploits, the arenas it appears in, the people who use it, the people it targets, and — above all — how to recognize and counter it.

**Purpose:** ground a *defense agent* you can consult about any suspected manipulation — by a partner, parent, boss, competitor, salesperson, advertiser, con artist, cult, or propagandist — and that answers with calibrated confidence, concrete counters, and honest caveats.

## What this is (and is not)

- **It is** a recognition-and-defense reference. Every entry leads with how to *spot* a tactic and what to *do* about it, at the level of detail used by published defensive literature (Cialdini, Freyd, Hassan, Bancroft, the FTC).
- **It is** epistemically careful. Evidence is graded (`established` → `contested`), weak pop-psychology constructs are flagged, and every tactic file has a **Caveats & false positives** section — because a tool that sees manipulation everywhere is itself harmful. See [[epistemic-guardrails]].
- **It is not** a how-to manual for manipulating people, a diagnostic instrument for labeling real individuals, or a substitute for therapy, legal advice, or emergency services.

## If you are in danger now

- **US:** National Domestic Violence Hotline 1-800-799-7233 / [thehotline.org](https://www.thehotline.org) · 988 Suicide & Crisis Lifeline · Report fraud: [reportfraud.ftc.gov](https://reportfraud.ftc.gov), [ic3.gov](https://www.ic3.gov)
- **UK:** National Domestic Abuse Helpline 0808 2000 247 · Samaritans 116 123 · Action Fraud 0300 123 2040
- **Cult/high-control group exit:** [ICSA](https://www.icsahome.com) · [Freedom of Mind](https://freedomofmind.com)
- Elsewhere: search "domestic violence hotline" + your country.

## How the knowledge base is organized

Seven entity types answer seven questions. One concept = one file = one stable kebab-case `id`.

| Folder | Type | Question it answers |
|---|---|---|
| `mechanisms/` | mechanism | **Why** does it work? (psychological levers: [[reciprocity]], [[intermittent-reinforcement]]…) |
| `tactics/` | tactic | **What** do they do? (observable moves: [[gaslighting]], [[love-bombing]], [[lowballing]]…) |
| `dynamics/` | dynamic | **How** does it unfold over time? ([[abuse-cycle]], [[con-anatomy]], [[grooming-sequence]]…) |
| `contexts/` | context | **Where** does it happen? (arena dossiers: [[workplace-bosses]], [[sales]], [[cults-high-control]]…) |
| `profiles/` | profile | **Who** does it? ([[dark-triad-overview]], [[con-artist-typologies]], [[everyday-manipulators]]…) |
| `vulnerabilities/` | vulnerability | **Who's targeted, and why them, why now?** ([[crisis-windows]], [[people-pleasing-fawn]]…) |
| `defenses/` | defense | **What do I do about it?** ([[gray-rock]], [[documentation-practices]], [[verification-rituals]]…) |
| `meta/` | meta | Epistemics: [[manipulation-vs-influence]], [[epistemic-guardrails]] |

Connections are explicit, typed, and machine-readable (in each file's YAML frontmatter): which tactics **exploit** which mechanisms, **co-occur with** each other, **escalate to** what, are **countered by** which defenses, and must be **distinguished from** which innocent look-alikes. `tools/kb.py` compiles them into `graph/edges.yaml` and human-readable matrices in `graph/`.

## How to use it

**As a human:**
- Open this folder as an **Obsidian vault** — wikilinks, backlinks, and the graph view work out of the box.
- Start at [[master-taxonomy]] (the map), or jump straight to a context dossier that matches your situation.
- Worried about a specific interaction? Each tactic file's **Recognition** section includes behavioral markers, typical phrases, and *felt-sense indicators* (what the target feels).
- Always read the **Caveats & false positives** section before concluding anything about a real person.

**As an AI:**
- Read `CLAUDE.md` (operating manual: schema, query cookbook, authoring pipeline, resume protocol).

## Status

Built topic-by-topic per `METHODOLOGY.md`; progress tracked in `ROADMAP.md` (~147 topics across 8 tiers). Run `python3 tools/kb.py stats` for live coverage. **Checkpoint 1 (2026-06-12):** 19/147 complete — foundations + 16/23 mechanisms, all red-teamed and citation-verified; 104 compiled edges; five-scenario retrieval spot-test passed (correct mechanisms and caveats surfaced for the boss/partner/crypto/church/deadline scenarios). **Checkpoint 2 (2026-06-20):** 62/147 complete — **Tiers 0–2 done**: foundations + 23 mechanisms + 33 cross-domain tactics + the 3 keystone defenses (detection-heuristics, boundary-scripts, verification-rituals); ~660 compiled edges; all red-teamed; retrieval spot-tests confirm tactic→counter wiring (every tactic routes to its keystone defense). Next: Tier 3 dynamics. **Checkpoint 3 (2026-06-20):** 72/147 complete — **Tiers 0–3 done** (the full conceptual core); all 10 dynamics added across three clusters (intimate-abuse: abuse-cycle/trauma-bonding/coercive-control/grooming-sequence; fraud: con-anatomy/romance-scam-arc/mlm-lifecycle; ideological/entrapment: cult-conversion-funnel/radicalization-pipeline/escalation-entrapment); ~810 compiled edges; all red-teamed with contested constructs (cult "brainwashing", radicalization pathways, the abuse cycle) graded honestly and DV/CSA/crisis files safety-flagged. Next: Tier 4 context dossiers + domain-specific tactics.

## Ethics

This knowledge base documents manipulation the way security research documents attacks: because defenders need the playbook more than attackers do (attackers already have it). Entries describe mechanics sufficient for recognition and defense, lead with counters, flag weak evidence, and insist on alternative innocent explanations. Label behaviors, not people; patterns, not incidents.

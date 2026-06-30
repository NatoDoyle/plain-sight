# Plain Sight

*Manipulation works by staying hidden — this is the field guide that drags it into plain sight.*

A defensive knowledge base on manipulation: every major tactic, the psychological mechanisms it exploits, the arenas it appears in, the people who use it, the people it targets, and — above all — how to recognize and counter it.

**Purpose:** ground a *defense agent* you can consult about any suspected manipulation — by a partner, parent, boss, competitor, salesperson, advertiser, con artist, cult, or propagandist — that answers with calibrated confidence, concrete counters, and honest caveats.

---

## ⚠️ If you are in danger right now

Read this before anything else. **If you are in immediate danger, call your local emergency number (US/UK: 911 / 999).**

- **US:** National Domestic Violence Hotline **1-800-799-7233** (text START to 88788) / [thehotline.org](https://www.thehotline.org) · **988** Suicide & Crisis Lifeline (call or text) · National Human Trafficking Hotline **1-888-373-7888** · Report fraud: [reportfraud.ftc.gov](https://reportfraud.ftc.gov), [ic3.gov](https://www.ic3.gov)
- **UK:** National Domestic Abuse Helpline **0808 2000 247** · Samaritans **116 123** · Action Fraud **0300 123 2040**
- **Cult / high-control group exit:** [ICSA](https://www.icsahome.com) · [Freedom of Mind](https://freedomofmind.com)
- **Elsewhere:** search "domestic violence hotline" + your country.

> If you might be monitored, assume a shared or gifted device could be watched. Reach out from a device the other person can't access (a friend's phone, a library computer).

---

## What this is (and is not)

- **It is** a recognition-and-defense reference. Every entry leads with how to *spot* a tactic and what to *do* about it, at the level of detail used by published defensive literature (Cialdini, Freyd, Hassan, Bancroft, the FTC).
- **It is** epistemically careful. Evidence is graded (`established` → `contested`), weak pop-psychology constructs are flagged, and every tactic file has a **Caveats & false positives** section — because a tool that sees manipulation everywhere is itself harmful.
- **It is not** a how-to manual for manipulating people, a way to diagnose a real individual with a disorder, or a substitute for therapy, legal advice, or emergency services. It labels *behaviors*, not people.

---

## 🚀 Getting started (never used GitHub or Obsidian? start here)

This project is just a folder of plain-text files. You can read it three ways — easiest first.

### Option 1 — Read it right here on GitHub (install nothing)

Scroll up to the file list at the top of this page, click a folder (e.g. **`tactics/`**), then click any file (e.g. `gaslighting.md`) to read it. The `[[double-bracket]]` links won't be clickable on GitHub, but everything is readable. Great for a quick look.

### Option 2 — Open it in Obsidian (recommended — clickable, searchable, with a visual map)

**Obsidian** is a free app that turns this folder into a connected web of notes: the `[[links]]` become clickable, search is instant, and a graph view shows how everything relates.

**Step 1 — Download the files to your computer.**
- On this page, click the green **`<> Code`** button (top right of the file list) → **Download ZIP**.
- Find the downloaded `plain-sight-main.zip`, double-click it to unzip, and you'll get a folder called `plain-sight-main` (rename it to `plain-sight` if you like). Remember where you put it.

**Step 2 — Install Obsidian (free).**
- Go to **[obsidian.md](https://obsidian.md)** → click **Download** → install it like any normal app (Windows, macOS, or Linux) → open it.

**Step 3 — Open the folder as a "vault".**
- A *vault* is just Obsidian's word for "a folder of notes."
- On Obsidian's start screen, click **Open folder as vault** → select the `plain-sight` folder you unzipped → **Open**.
- If Obsidian asks whether to **Trust author and enable plugins**, you can trust it — these are plain text files; no code runs. (You don't need any plugins to read it.)

**Step 4 — Look around.**
- **Search** anything (click the 🔍 icon, or press `Ctrl/Cmd + Shift + F`): try how it *feels* — `walking on eggshells`, `too good to be true`, `confused after every conversation`.
- **Click any `[[link]]`** to jump to that note; use the back arrow (top left) to return.
- **Graph view** (the connected-dots icon in the left sidebar): see the whole web of connections and zoom into any cluster.
- Lost? Press `Ctrl/Cmd + P` for the command palette.

**Step 5 — Where to start reading.**
- **`taxonomy/felt-sense-index.md`** — start here if you only know how a situation *feels*. It maps feelings → likely patterns.
- **`taxonomy/master-taxonomy.md`** — the map of the entire knowledge base.
- **`contexts/`** — pick the arena that matches you: `intimate-relationships`, `family-parents`, `workplace-bosses`, `sales`, `scams-fraud`, `cults-high-control`, …
- **Always read a file's "Caveats & false positives" section** before drawing conclusions about a real person — most behaviors have an innocent explanation too.

### Option 3 — Open the files in any text editor

Every file is plain **Markdown** (`.md`). Open them in Notepad, TextEdit, VS Code — anything. Readable, though the `[[links]]` won't be clickable.

### Want updates later? (optional — uses Git)

If you'd like to *pull updates* instead of re-downloading the ZIP: install **[Git](https://git-scm.com/downloads)**, then in a terminal run

```
git clone https://github.com/NatoDoyle/plain-sight.git
```

Later, `cd plain-sight` and run `git pull` to get the latest. (This is optional — the ZIP download above is perfectly fine.)

---

## How the knowledge base is organized

Seven entity types answer seven questions. One concept = one file = one stable kebab-case `id`.

| Folder | Type | Question it answers |
|---|---|---|
| `mechanisms/` | mechanism | **Why** does it work? (psychological levers: `reciprocity`, `intermittent-reinforcement`…) |
| `tactics/` | tactic | **What** do they do? (observable moves: `gaslighting`, `love-bombing`, `lowballing`…) |
| `dynamics/` | dynamic | **How** does it unfold over time? (`abuse-cycle`, `con-anatomy`, `grooming-sequence`…) |
| `contexts/` | context | **Where** does it happen? (arena dossiers: `workplace-bosses`, `sales`, `cults-high-control`…) |
| `profiles/` | profile | **Who** does it? (`dark-triad-overview`, `con-artist-typologies`, `everyday-manipulators`…) |
| `vulnerabilities/` | vulnerability | **Who's targeted, and why them, why now?** (`crisis-windows`, `people-pleasing-fawn`…) |
| `defenses/` | defense | **What do I do about it?** (`gray-rock`, `documentation-practices`, `verification-rituals`…) |
| `meta/`, `taxonomy/` | meta | The map, the boundaries, and the synthesis (`felt-sense-index`, `playbooks-compendium`, `defense-agent-spec`) |

Connections are explicit, typed, and machine-readable (in each file's YAML frontmatter): which tactics **exploit** which mechanisms, **co-occur with** each other, **escalate to** what, are **countered by** which defenses, and must be **distinguished from** which innocent look-alikes. `tools/kb.py` compiles them into `graph/edges.yaml` and human-readable matrices in `graph/`.

## How to use it

**As a human:** open the folder in Obsidian (above), search by how it feels, follow the links, and read the caveats. Start at `taxonomy/felt-sense-index.md` or a context dossier that matches your situation.

**As an AI / developer:** read `CLAUDE.md` (the operating manual: schema, query cookbook, authoring pipeline). The capstone `meta/defense-agent-spec.md` is a drop-in system prompt + retrieval strategy + safety-escalation rules for building the defense agent this KB exists to power. Run `python3 tools/kb.py stats` (no installs needed — standard library only) for live coverage.

## Status — ✅ complete

All **147 topics across 8 tiers** are written, cross-linked, evidence-graded, and safety-checked. `python3 tools/kb.py validate` → **147 files, 0 errors, 0 warnings**. Snapshot: **23** mechanisms · **65** tactics · **10** dynamics · **12** contexts · **6** profiles · **9** vulnerabilities · **15** defenses · **7** meta/synthesis. **1,221** typed connections; **49** files carry crisis-safety guidance with verified hotline resources; **78** "innocent look-alike" contrast concepts guard against false positives; evidence honestly graded (29 established / 88 supported / 14 clinical / 6 contested / 5 folk), with every contested and folk construct flagged inline. See `ROADMAP.md` for the tier-by-tier map and `taxonomy/coverage-audit.md` for an honest gap analysis.

<details>
<summary><strong>Full build history (checkpoints 1–6)</strong></summary>

Built topic-by-topic per `METHODOLOGY.md`.

**Checkpoint 1 (2026-06-12):** 19/147 — foundations + 16/23 mechanisms, all red-teamed and citation-verified; 104 compiled edges; five-scenario retrieval spot-test passed (boss/partner/crypto/church/deadline).

**Checkpoint 2 (2026-06-20):** 62/147 — **Tiers 0–2 done**: foundations + 23 mechanisms + 33 cross-domain tactics + 3 keystone defenses (detection-heuristics, boundary-scripts, verification-rituals); ~660 edges; every tactic routes to its keystone defense.

**Checkpoint 3 (2026-06-20):** 72/147 — **Tiers 0–3 done** (full conceptual core); all 10 dynamics across three clusters (intimate-abuse, fraud, ideological/entrapment); ~810 edges; contested constructs ("brainwashing", radicalization pathways, the abuse cycle) graded honestly; DV/CSA/crisis files safety-flagged.

**Checkpoint 4 (2026-06-27):** 112/147 — **Tier 4a done** (12 context dossiers) + most of Tier 4b (28 domain tactics incl. the full fraud cluster); ~1,070 edges; fast-moving legal facts re-verified to 2026 (vacated CARS Rule, Amazon $2.5B, the Madoff $64.8B-fictional-vs-$17.5B-principal rule, AI-fraud hype flagged as projections); AI sextortion safety-flagged.

**Checkpoint 5 (2026-06-30):** 129/147 — **Tiers 0–5 done**: Tier 4 closed (propaganda, graded for *overstated* mass-persuasion effects) + all of Tier 5 (6 profiles, 9 vulnerabilities); ~1,170 edges (new `favored-by` and `targets` relations). Profiles carry maximal anti-diagnosis discipline (Goldwater Rule); vulnerabilities carry maximal anti-victim-blaming discipline (`why-smart-people-fall` keystone).

**✅ Checkpoint 6 — COMPLETE (2026-06-30): 147/147 across all 8 tiers.** Tier 6 closed all 15 defenses; Tier 4b finished (fud-competitor-tactics, bad-faith-negotiation); and **Tier 7 — the synthesis finale — is in:** `felt-sense-index` (feeling → candidate patterns, every entry caveated), `playbooks-compendium` (named multi-tactic sequences + the universal arc), `defense-agent-spec` (the drop-in system prompt that grounds the future defense agent), and `coverage-audit` (honest final gap analysis). 1,221 compiled edges; 49 safety-flagged files; 78 false-positive contrast concepts. The knowledge base is complete to spec; remaining work is maintenance — localize crisis/legal resources beyond US/UK, refresh fast-moving files, and thicken the causal-edge layer (see `coverage-audit`).

</details>

## Ethics

This knowledge base documents manipulation the way security research documents attacks: because defenders need the playbook more than attackers do (attackers already have it). Entries describe mechanics sufficient for recognition and defense, lead with counters, flag weak evidence, and insist on alternative innocent explanations. **Label behaviors, not people; patterns, not incidents.** Nothing here is therapy, legal advice, or a tool for diagnosing a real person.

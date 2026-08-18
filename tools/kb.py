#!/usr/bin/env python3
"""Plain Sight KB toolchain (stdlib only).

Commands:
  validate  schema, enums, id=filename, edge/wikilink resolution, section gates,
            safety-flag symmetry, prose-wikilink-to-contrast-concept warnings
  graph     compile typed edges from frontmatter -> graph/edges.yaml
  matrix    regenerate graph/tactic-mechanism.md and graph/tactic-context.md
  stats     coverage by type/status, edge counts, ROADMAP cross-check
  eval      Layer A of meta/agent-evals.md: retrieval-doorway registration and
            coverage, scenario id resolution, entry-path reachability,
            discriminator availability, safety routing, per-kind field gates

Frontmatter is a constrained YAML subset: flat keys; scalar values or lists of
plain strings (flow `[a, b]` or block `- a` style); no nesting, no inline
comments. See CLAUDE.md.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONTENT_DIRS = {
    "mechanisms": {"mechanism"},
    "tactics": {"tactic"},
    "dynamics": {"dynamic"},
    "contexts": {"context"},
    "profiles": {"profile"},
    "vulnerabilities": {"vulnerability"},
    "defenses": {"defense"},
    "meta": {"meta"},
    "taxonomy": {"meta"},
}
SKIP = {"taxonomy/glossary.md"}

EVAL_FILE = "meta/agent-evals.md"
SKILL_FILE = ".claude/skills/defense-agent/SKILL.md"

# Retrieval doorways the agent is told to walk. role: entry = how a person gets in;
# expand = how the agent widens once inside. Every doorway path MUST appear verbatim
# in SKILL_FILE -- that coupling is the point of this check.
DOORWAYS = {
    "taxonomy/felt-sense-index.md":     "entry",
    "taxonomy/bias-codex-index.md":     "entry",
    "taxonomy/master-taxonomy.md":      "expand",
    "taxonomy/playbooks-compendium.md": "expand",
    "taxonomy/glossary.md":             "expand",
}
# taxonomy/ files that are deliberately NOT lookup paths. A reason is required.
DOORWAY_EXEMPT = {
    "taxonomy/coverage-audit.md":    "audit artifact, not a lookup path",
    "taxonomy/emergent-insights.md": "synthesis essay, not a lookup path",
}
DOOR_COVERAGE_TYPES = {"mechanism", "tactic", "dynamic"}
KINDS = {"detection", "look-alike", "safety", "named-construct",
         "weaponization", "third-party"}

TYPES = {"mechanism", "tactic", "dynamic", "context", "profile",
         "vulnerability", "defense", "meta"}
STATUSES = {"backlog", "researching", "drafted", "reviewed", "complete",
            "needs-update"}
EVIDENCE = {"established", "supported", "clinical", "folk", "contested"}
SEVERITY = {"low", "medium", "high", "critical"}
EVIDENCE_REQUIRED = {"tactic", "mechanism", "dynamic", "profile",
                     "vulnerability", "defense"}
CAVEATS_REQUIRED = {"tactic", "dynamic", "context", "profile", "vulnerability"}

EDGE_FIELDS = {  # frontmatter field -> relation name in the compiled graph
    "exploits": "exploits",
    "domains": "appears-in",
    "co-occurs-with": "co-occurs-with",
    "precedes": "precedes",
    "escalates-to": "escalates-to",
    "enables": "enables",
    "countered-by": "countered-by",
    "distinguished-from": "distinguished-from",
    "variant-of": "variant-of",
    "favored-by": "favored-by",
    "targets": "targets",
    "composed-of": "composed-of",
}
SYMMETRIC = {"co-occurs-with", "distinguished-from"}
SCALAR_KEYS = {"id", "type", "name", "severity", "evidence", "safety",
               "status", "last-updated"}
LIST_KEYS = {"aliases"} | set(EDGE_FIELDS)

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
KEYLINE = re.compile(r"^([A-Za-z][A-Za-z0-9-]*):\s*(.*)$")
BLOCK_ITEM = re.compile(r"^\s+-\s+(.+)$")
WIKILINK = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
SAFETY_H = re.compile(r"(?m)^##\s+Safety notes\b")  # actual heading, not an inline mention
ROADMAP_ID = re.compile(r"^- \[[ xX]\] `([a-z0-9-]+)`", re.M)
ROADMAP_CHECKED = re.compile(r"^- \[[xX]\] `([a-z0-9-]+)`", re.M)
GLOSSARY_ID = re.compile(r"^- `([a-z0-9-]+)`", re.M)
FENCED = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")
SCENARIO_H = re.compile(r"^###\s+(EV-\d+)\s*(?:[—-]\s*)?(.*)$")
FIELD_LINE = re.compile(r"^\*\*([A-Za-z][A-Za-z -]*):\*\*\s*(.*)$")
TIER_H = re.compile(r"^##\s+Tier\s+(\d+)\b", re.M)
COVERS_TIERS = re.compile(r"\*\*Covers tiers:\*\*\s*0\s*[—–-]\s*(\d+)")
CODEX_ROW = re.compile(r"^\|([^|]+)\|\s*\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]\s*\|")
DASHED = re.compile(r"\s+[—–]\s+|\s+--\s+")


def strip_quotes(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1].strip()
    return s


def parse_frontmatter(text, relpath, problems):
    """Return (fm dict, body str) or (None, text) when no frontmatter."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    fm, i, end = {}, 1, None
    while i < len(lines):
        if lines[i].strip() == "---":
            end = i
            break
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = KEYLINE.match(line)
        if not m:
            problems.append(("ERROR", relpath, f"unparseable frontmatter line: {line!r}"))
            i += 1
            continue
        key, raw = m.group(1), m.group(2).strip()
        if raw.startswith("["):
            if not raw.endswith("]"):
                problems.append(("ERROR", relpath, f"{key}: flow list must close on one line"))
                fm[key] = []
            else:
                inner = raw[1:-1].strip()
                fm[key] = [strip_quotes(x) for x in inner.split(",") if x.strip()] if inner else []
            i += 1
        elif raw == "":
            items = []
            j = i + 1
            while j < len(lines) and lines[j].strip() != "---" and BLOCK_ITEM.match(lines[j]):
                items.append(strip_quotes(BLOCK_ITEM.match(lines[j]).group(1)))
                j += 1
            fm[key] = items  # empty value with no items = empty list
            i = j
        else:
            fm[key] = strip_quotes(raw)
            i += 1
    if end is None:
        problems.append(("ERROR", relpath, "frontmatter never closed with ---"))
        return fm, ""
    return fm, "\n".join(lines[end + 1:])


def load_kb(problems):
    """Parse all content files. Returns list of records."""
    records = []
    for folder in sorted(CONTENT_DIRS):
        d = ROOT / folder
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            rel = f"{folder}/{path.name}"
            if rel in SKIP:
                continue
            fm, body = parse_frontmatter(path.read_text(encoding="utf-8"), rel, problems)
            if fm is None:
                problems.append(("ERROR", rel, "missing frontmatter"))
                continue
            records.append({"rel": rel, "folder": folder, "stem": path.stem,
                            "fm": fm, "body": body})
    return records


def load_targets(records):
    """Known link/edge targets: file ids, aliases, roadmap ids, glossary contrast ids."""
    ids = {r["fm"].get("id") for r in records if r["fm"].get("id")}
    aliases = {}
    for r in records:
        for a in r["fm"].get("aliases", []) if isinstance(r["fm"].get("aliases", []), list) else []:
            aliases[a.casefold()] = r["fm"].get("id", r["stem"])
    roadmap = set()
    rp = ROOT / "ROADMAP.md"
    if rp.exists():
        roadmap = set(ROADMAP_ID.findall(rp.read_text(encoding="utf-8")))
    contrast = set()
    gp = ROOT / "taxonomy" / "glossary.md"
    if gp.exists():
        contrast = set(GLOSSARY_ID.findall(gp.read_text(encoding="utf-8")))
    return ids, aliases, roadmap, contrast


def resolve(target, ids, aliases, roadmap, contrast):
    """Classify a link/edge target."""
    if target in ids:
        return "id"
    if target.casefold() in aliases:
        return "alias"
    if target in contrast:
        return "contrast"
    if target in roadmap:
        return "pending"
    return None


def collect_edges(records, ids, aliases):
    """All declared edges with aliases canonicalized. Returns sorted unique list."""
    edges = set()
    for r in records:
        src = r["fm"].get("id", r["stem"])
        for field, rel in EDGE_FIELDS.items():
            vals = r["fm"].get(field, [])
            if not isinstance(vals, list):
                continue
            for t in vals:
                t_id = aliases.get(t.casefold(), t)
                edges.add((src, rel, t_id))
                if rel in SYMMETRIC:
                    edges.add((t_id, rel, src))
    return sorted(edges)


def cmd_validate():
    problems = []
    records = load_kb(problems)
    ids_seen = {}
    for r in records:
        fm, rel = r["fm"], r["rel"]
        fid = fm.get("id", "")
        ftype = fm.get("type", "")
        status = fm.get("status", "")
        # required scalars
        for key in ("id", "type", "name", "status", "last-updated"):
            if not fm.get(key):
                problems.append(("ERROR", rel, f"missing required field: {key}"))
        # key sanity
        for key, val in fm.items():
            if key in SCALAR_KEYS and isinstance(val, list):
                problems.append(("ERROR", rel, f"{key}: expected scalar, got list"))
            elif key in LIST_KEYS and not isinstance(val, list):
                problems.append(("ERROR", rel, f"{key}: expected list, got scalar"))
            elif key not in SCALAR_KEYS | LIST_KEYS:
                problems.append(("WARN", rel, f"unknown frontmatter key: {key}"))
        # id rules
        if fid:
            if not KEBAB.match(fid):
                problems.append(("ERROR", rel, f"id not kebab-case: {fid}"))
            if fid != r["stem"]:
                problems.append(("ERROR", rel, f"id {fid!r} != filename stem {r['stem']!r}"))
            if fid in ids_seen:
                problems.append(("ERROR", rel, f"duplicate id (also in {ids_seen[fid]})"))
            ids_seen[fid] = rel
        # enums
        if ftype and ftype not in TYPES:
            problems.append(("ERROR", rel, f"illegal type: {ftype}"))
        if ftype in TYPES and ftype not in CONTENT_DIRS[r["folder"]]:
            problems.append(("ERROR", rel, f"type {ftype} not allowed in {r['folder']}/"))
        if status and status not in STATUSES:
            problems.append(("ERROR", rel, f"illegal status: {status}"))
        if fm.get("evidence") and fm["evidence"] not in EVIDENCE:
            problems.append(("ERROR", rel, f"illegal evidence grade: {fm['evidence']}"))
        if ftype in EVIDENCE_REQUIRED and not fm.get("evidence"):
            problems.append(("ERROR", rel, f"evidence grade required for type {ftype}"))
        if fm.get("severity") and fm["severity"] not in SEVERITY:
            problems.append(("ERROR", rel, f"illegal severity: {fm['severity']}"))
        lu = fm.get("last-updated", "")
        if lu and not DATE.match(str(lu)):
            problems.append(("ERROR", rel, f"last-updated not YYYY-MM-DD: {lu}"))
        # section gates (hard once complete, soft before)
        level = "ERROR" if status == "complete" else "WARN"
        if ftype in CAVEATS_REQUIRED and "## Caveats" not in r["body"]:
            problems.append((level, rel, "missing '## Caveats' section"))
        if fm.get("safety") and not SAFETY_H.search(r["body"]):
            problems.append((level, rel, "safety-flagged but no '## Safety notes' section"))
        if not fm.get("safety") and SAFETY_H.search(r["body"]):
            problems.append((level, rel, "has '## Safety notes' section but missing 'safety:' flag"))
        if status == "complete" and "## Sources" not in r["body"]:
            problems.append(("ERROR", rel, "complete but no '## Sources' section"))
    # alias collisions
    ids, aliases, roadmap, contrast = load_targets(records)
    alias_owners = {}
    for r in records:
        for a in r["fm"].get("aliases", []) if isinstance(r["fm"].get("aliases", []), list) else []:
            if a in ids and a != r["fm"].get("id"):
                problems.append(("ERROR", r["rel"], f"alias {a!r} collides with an id"))
            alias_owners.setdefault(a.casefold(), []).append(r["rel"])
    for a, owners in sorted(alias_owners.items()):
        if len(owners) > 1:
            problems.append(("WARN", owners[0],
                             f"alias {a!r} declared in multiple files ({', '.join(owners)}); "
                             f"an alias must live on exactly one file"))
    # edge + wikilink resolution
    pending = set()
    for r in records:
        rel_path = r["rel"]
        for field in EDGE_FIELDS:
            vals = r["fm"].get(field, [])
            if not isinstance(vals, list):
                continue
            for t in vals:
                kind = resolve(t, ids, aliases, roadmap, contrast)
                if kind is None:
                    problems.append(("ERROR", rel_path,
                                     f"{field}: unknown target {t!r} (not an id/alias/ROADMAP id/glossary contrast)"))
                elif kind == "pending":
                    pending.add(t)
                elif kind == "alias":
                    problems.append(("WARN", rel_path,
                                     f"{field}: {t!r} is an alias; prefer canonical id {aliases[t.casefold()]!r}"))
        body = INLINE_CODE.sub("", FENCED.sub("", r["body"]))
        for m in WIKILINK.finditer(body):
            t = m.group(1).strip()
            kind = resolve(t, ids, aliases, roadmap, contrast)
            if kind is None:
                problems.append(("ERROR", rel_path, f"wikilink to unknown target [[{t}]]"))
            elif kind == "pending":
                pending.add(t)
            elif kind == "contrast":
                problems.append(("WARN", rel_path,
                                 f"wikilink [[{t}]] targets a contrast concept (no file -> "
                                 f"unresolved/phantom node in Obsidian); use plain text"))
    errors = [p for p in problems if p[0] == "ERROR"]
    warns = [p for p in problems if p[0] == "WARN"]
    for lvl, rel_path, msg in problems:
        print(f"{lvl:5} {rel_path}: {msg}")
    print(f"\nvalidate: {len(records)} files, {len(errors)} errors, "
          f"{len(warns)} warnings, {len(pending)} pending (backlog) link targets")
    return 1 if errors else 0


def cmd_graph():
    problems = []
    records = load_kb(problems)
    ids, aliases, _, _ = load_targets(records)
    edges = collect_edges(records, ids, aliases)
    out = ROOT / "graph" / "edges.yaml"
    lines = ["# Generated by `python3 tools/kb.py graph` -- do not edit by hand.",
             f"# {len(edges)} edges (symmetric relations expanded both directions)",
             "edges:"]
    for a, rel, b in edges:
        lines.append(f"  - {{from: {a}, rel: {rel}, to: {b}}}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"graph: wrote {len(edges)} edges -> graph/edges.yaml")
    return 0


def _matrix(records, ids, aliases, rel_name, by_to_title, by_from_title, outfile, title):
    edges = [e for e in collect_edges(records, ids, aliases) if e[1] == rel_name]
    by_to, by_from = {}, {}
    for a, _, b in edges:
        by_to.setdefault(b, []).append(a)
        by_from.setdefault(a, []).append(b)
    lines = [f"# {title}", "",
             "> Generated by `python3 tools/kb.py matrix` -- do not edit by hand.", "",
             f"## {by_to_title}", ""]
    for b in sorted(by_to):
        lines.append(f"### [[{b}]]")
        for a in sorted(set(by_to[b])):
            lines.append(f"- [[{a}]]")
        lines.append("")
    lines += [f"## {by_from_title}", ""]
    for a in sorted(by_from):
        targets = ", ".join(f"[[{b}]]" for b in sorted(set(by_from[a])))
        lines.append(f"- [[{a}]] → {targets}")
    (ROOT / "graph" / outfile).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"matrix: wrote graph/{outfile} ({len(edges)} {rel_name} edges)")


def cmd_matrix():
    problems = []
    records = load_kb(problems)
    ids, aliases, _, _ = load_targets(records)
    _matrix(records, ids, aliases, "exploits",
            "By mechanism (which moves pull this lever)",
            "By tactic (which levers this move pulls)",
            "tactic-mechanism.md", "Tactic ⇄ Mechanism map")
    _matrix(records, ids, aliases, "appears-in",
            "By context (what operates in this arena)",
            "By tactic (where this move appears)",
            "tactic-context.md", "Tactic ⇄ Context map")
    return 0


def cmd_stats():
    problems = []
    records = load_kb(problems)
    ids, aliases, roadmap, contrast = load_targets(records)
    by_type, by_status = {}, {}
    for r in records:
        by_type[r["fm"].get("type", "?")] = by_type.get(r["fm"].get("type", "?"), 0) + 1
        by_status[r["fm"].get("status", "?")] = by_status.get(r["fm"].get("status", "?"), 0) + 1
    print(f"files: {len(records)}")
    print("by type:   " + ", ".join(f"{k}={v}" for k, v in sorted(by_type.items())))
    print("by status: " + ", ".join(f"{k}={v}" for k, v in sorted(by_status.items())))
    edges = collect_edges(records, ids, aliases)
    by_rel = {}
    for _, rel, _ in edges:
        by_rel[rel] = by_rel.get(rel, 0) + 1
    print("edges:     " + (", ".join(f"{k}={v}" for k, v in sorted(by_rel.items())) or "none"))
    # ROADMAP cross-check
    rp = ROOT / "ROADMAP.md"
    if rp.exists():
        text = rp.read_text(encoding="utf-8")
        all_ids = ROADMAP_ID.findall(text)
        checked = set(ROADMAP_CHECKED.findall(text))
        complete = {r["fm"].get("id") for r in records if r["fm"].get("status") == "complete"}
        print(f"roadmap:   {len(checked)}/{len(all_ids)} checked")
        for i in sorted(complete - checked):
            if i in set(all_ids):
                print(f"MISMATCH: {i} is complete but unchecked in ROADMAP.md")
        for i in sorted(checked - complete):
            print(f"MISMATCH: {i} checked in ROADMAP.md but file missing or not complete")
    return 0


def _norm(s):
    """Tolerant form for heading/name matching: no quotes, no emphasis, flat dashes."""
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"[\"'*`]", "", s)
    return " ".join(s.split()).casefold()


def _split_list(raw):
    """Assertion lists use the ` · ` separator; the literal `none` is the empty set."""
    raw = (raw or "").strip()
    if raw.casefold() == "none":
        return []
    return [t.strip().strip("`").strip() for t in raw.split(" · ") if t.strip()]


def _is_none(tok):
    """`none`, alone or followed by an explanatory dash clause."""
    n = _norm(tok)
    return n == "none" or n.startswith("none ") or n.startswith("none-")


def _canon(t, aliases):
    return aliases.get(t.casefold(), t)


def _route_files(raw):
    """Safety-route tokens are `<file id> — resources` or bare resource text."""
    out = []
    for tok in _split_list(raw):
        head = DASHED.split(tok, 1)[0].strip().rstrip(",.;:")
        if KEBAB.match(head):
            out.append(head)
    return out


def parse_scenarios(body):
    """Return [{id, title, line, fields}] for every `### EV-NN` block."""
    out, cur, last = [], None, None
    for n, line in enumerate(body.split("\n"), 1):
        m = SCENARIO_H.match(line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2).strip(), "line": n, "fields": {}}
            out.append(cur)
            last = None
            continue
        if line.startswith("#"):
            cur, last = None, None
            continue
        if cur is None:
            continue
        m = FIELD_LINE.match(line)
        if m:
            last = m.group(1).strip()
            cur["fields"][last] = m.group(2).strip()
        elif line.strip() and last:
            cur["fields"][last] += " " + line.strip()
    return out


def load_doorway_blocks():
    """(felt-sense heading -> wikilink targets, codex entry name -> home id)."""
    felt, codex = {}, {}
    fp = ROOT / "taxonomy" / "felt-sense-index.md"
    if fp.exists():
        cur = None
        for line in fp.read_text(encoding="utf-8").split("\n"):
            if line.startswith("### "):
                cur = _norm(line[4:])
                felt.setdefault(cur, set())
            elif line.startswith("#"):
                cur = None
            elif cur is not None:
                for m in WIKILINK.finditer(line):
                    felt[cur].add(m.group(1).strip())
    cp = ROOT / "taxonomy" / "bias-codex-index.md"
    if cp.exists():
        for line in cp.read_text(encoding="utf-8").split("\n"):
            m = CODEX_ROW.match(line)
            if m:
                codex[_norm(m.group(1))] = m.group(2).strip()
    return felt, codex


def _lookup(table, needle):
    """Exact match, else unique prefix match. Returns (key or None, status)."""
    if needle in table:
        return needle, "ok"
    hits = sorted(k for k in table if k.startswith(needle))
    if len(hits) == 1:
        return hits[0], "ok"
    if len(hits) > 1:
        return None, "ambiguous"
    return None, "unknown"


def cmd_eval():
    problems = []
    records = load_kb(problems)
    ids, aliases, roadmap, contrast = load_targets(records)
    edges = collect_edges(records, ids, aliases)
    by_id = {r["fm"].get("id", r["stem"]): r for r in records}
    alias_norm = {_norm(a): owner for a, owner in aliases.items()}
    discriminators = {(a, b) for a, rel, b in edges if rel == "distinguished-from"}
    felt, codex = load_doorway_blocks()

    # --- corpus: every registered doorway is named in the skill
    skill = ROOT / SKILL_FILE
    skill_text = skill.read_text(encoding="utf-8") if skill.exists() else ""
    if not skill.exists():
        problems.append(("ERROR", SKILL_FILE, "skill file missing; no doorway can be walked"))
    for path, role in sorted(DOORWAYS.items()):
        if path not in skill_text:
            problems.append(("ERROR", SKILL_FILE,
                             f"registered {role} doorway {path} is never named in the skill "
                             f"— the agent is not told to walk it"))
    # --- corpus: every taxonomy file is classified
    for p in sorted((ROOT / "taxonomy").glob("*.md")):
        rel = f"taxonomy/{p.name}"
        if rel not in DOORWAYS and rel not in DOORWAY_EXEMPT:
            problems.append(("ERROR", rel,
                             "new taxonomy file is neither a registered DOORWAY nor "
                             "DOORWAY_EXEMPT in tools/kb.py — classify it"))
    # --- corpus: everything findable is reachable from some doorway
    reachable = set()
    for path in sorted(DOORWAYS):
        fp = ROOT / path
        if not fp.exists():
            problems.append(("ERROR", path, "registered doorway file does not exist"))
            continue
        for m in WIKILINK.finditer(fp.read_text(encoding="utf-8")):
            reachable.add(_canon(m.group(1).strip(), aliases))
    coverage = {t: [0, 0] for t in sorted(DOOR_COVERAGE_TYPES)}
    for r in records:
        ftype = r["fm"].get("type", "")
        if ftype not in DOOR_COVERAGE_TYPES:
            continue
        coverage[ftype][1] += 1
        if _canon(r["fm"].get("id", r["stem"]), aliases) in reachable:
            coverage[ftype][0] += 1
        else:
            problems.append(("ERROR", r["rel"],
                             "unreachable: appears in no registered retrieval doorway"))

    # --- the eval file itself
    ep = ROOT / EVAL_FILE
    if not ep.exists():
        problems.append(("ERROR", EVAL_FILE, "eval file missing; nothing to check"))
        return _report_eval(problems, [], coverage, None, None)
    text = ep.read_text(encoding="utf-8")
    _, ebody = parse_frontmatter(text, EVAL_FILE, problems)
    offset = len(text.split("\n")) - len(ebody.split("\n"))
    scenarios = parse_scenarios(ebody)

    # --- tier freshness
    rmax = None
    rp = ROOT / "ROADMAP.md"
    if rp.exists():
        tiers = [int(t) for t in TIER_H.findall(rp.read_text(encoding="utf-8"))]
        rmax = max(tiers) if tiers else None
    m = COVERS_TIERS.search(ebody)
    declared = int(m.group(1)) if m else None
    if declared is None:
        problems.append(("ERROR", EVAL_FILE,
                         "no '**Covers tiers:** 0-N' declaration — the suite does not say "
                         "what it covers"))
    elif rmax is not None and declared < rmax:
        problems.append(("ERROR", EVAL_FILE,
                         f"declares '**Covers tiers:** 0-{declared}' but ROADMAP.md now reaches "
                         f"Tier {rmax} — add scenarios for the new tier(s), then bump the "
                         f"declaration"))

    # --- every safety flag in the corpus is exercised by a gate
    gates, doorway_prefixes = set(), set()
    for sc in scenarios:
        raw = sc["fields"].get("Safety-gate", "none")
        gates.add("none" if _is_none(raw) else raw.strip())
        for tok in _split_list(sc["fields"].get("Entry-path", "none")):
            if not _is_none(tok):
                doorway_prefixes.add(_norm(tok.partition("#")[0]))
    for flag in sorted({r["fm"].get("safety") for r in records if r["fm"].get("safety")}):
        if flag not in gates:
            problems.append(("ERROR", EVAL_FILE,
                             f"safety flag {flag!r} is used in the corpus but no scenario "
                             f"exercises it as a Safety-gate — an untested gate"))
    # --- every entry-role doorway is entered by a scenario
    for path, role in sorted(DOORWAYS.items()):
        if role != "entry":
            continue
        stem = Path(path).stem
        if stem.endswith("-index"):
            stem = stem[:-len("-index")]
        if stem not in doorway_prefixes:
            problems.append(("ERROR", EVAL_FILE,
                             f"no scenario enters through {stem}# ({path}) — the entry doorway "
                             f"is never exercised"))

    by_kind = {}
    for sc in scenarios:
        f, sid = sc["fields"], sc["id"]
        rel = f"{EVAL_FILE}:{sc['line'] + offset}"
        kind = f.get("Kind", "").strip()
        by_kind[kind or "?"] = by_kind.get(kind or "?", 0) + 1
        must = _split_list(f.get("Must-surface", "none"))
        should = _split_list(f.get("Should-surface", "none"))
        mustnot = _split_list(f.get("Must-not-surface", "none"))
        caveats = _split_list(f.get("Must-caveat", "none"))
        route = _route_files(f.get("Safety-route", "none"))
        entry = [t for t in _split_list(f.get("Entry-path", "none")) if not _is_none(t)]
        gate_raw = f.get("Safety-gate", "none")
        gate = "none" if _is_none(gate_raw) else gate_raw.strip()
        c_must = {_canon(t, aliases) for t in must}
        c_mustnot = {_canon(t, aliases) for t in mustnot}

        # R1 -- every asserted token resolves
        for field, toks in (("Must-surface", must), ("Should-surface", should),
                            ("Must-not-surface", mustnot), ("Must-caveat", caveats),
                            ("Safety-route", route)):
            for t in toks:
                kres = resolve(t, ids, aliases, roadmap, contrast)
                if kres is None:
                    problems.append(("ERROR", rel,
                                     f"{sid} R1 {field}: unknown target {t!r} (not an "
                                     f"id/alias/ROADMAP id/glossary contrast)"))
                elif kres == "alias":
                    problems.append(("WARN", rel,
                                     f"{sid} R1 {field}: {t!r} is an alias; prefer canonical "
                                     f"id {aliases[t.casefold()]!r}"))
        # R7 -- an id cannot be both required and forbidden
        for t in sorted(c_must & c_mustnot):
            problems.append(("ERROR", rel,
                             f"{sid} R7: {t} is in both Must-surface and Must-not-surface"))
        # R2/R3 -- the doorway leads where the scenario says it does
        for tok in entry:
            prefix, sep, arg = tok.partition("#")
            prefix, arg = _norm(prefix), arg.strip()
            if not sep:
                problems.append(("ERROR", rel,
                                 f"{sid} R2 Entry-path: {tok!r} has no doorway prefix "
                                 f"(felt-sense# / bias-codex# / alias# / direct# / none)"))
            elif prefix == "felt-sense":
                k, status = _lookup(felt, _norm(arg))
                if status != "ok":
                    problems.append(("ERROR", rel,
                                     f"{sid} R2 Entry-path: felt-sense heading {arg!r} is "
                                     f"{status} in taxonomy/felt-sense-index.md"))
                    continue
                block = {_canon(t, aliases) for t in felt[k]}
                for t in sorted(c_must - block):
                    problems.append(("ERROR", rel,
                                     f"{sid} R3 Must-surface: {t} is NOT reachable from "
                                     f"felt-sense entry {k!r} — the doorway does not lead there"))
                # The exclusion half is scoped OUT for `Kind: look-alike`. For those
                # scenarios `Must-not-surface` is a Layer B assertion about the RESPONSE,
                # not a Layer A assertion about the doorway: the felt-sense index's job is
                # to offer candidate patterns, and ruling one out happens at retrieval
                # step 4 (Caveats + contrast concepts), not at the door. A look-alike is
                # precisely the case where the person's own words SHOULD reach the file
                # that then has to be ruled out — requiring the doorway to omit it would
                # break the index. Every other kind keeps the check: EV-07's
                # financial-abuse is the logged keyword-retrieval regression.
                if kind != "look-alike":
                    for t in sorted(c_mustnot & block):
                        problems.append(("ERROR", rel,
                                         f"{sid} R3 Must-not-surface: {t} IS reachable from "
                                         f"felt-sense entry {k!r} — over-detection path open"))
            elif prefix == "bias-codex":
                k, status = _lookup(codex, _norm(arg))
                if status != "ok":
                    problems.append(("ERROR", rel,
                                     f"{sid} R2 Entry-path: codex entry {arg!r} is {status} in "
                                     f"taxonomy/bias-codex-index.md"))
                elif _canon(codex[k], aliases) not in c_must:
                    problems.append(("ERROR", rel,
                                     f"{sid} R3 Entry-path: codex entry {k!r} homes to "
                                     f"{codex[k]}, which is not in Must-surface"))
            elif prefix == "alias":
                owner = alias_norm.get(_norm(arg))
                if owner is None:
                    problems.append(("ERROR", rel,
                                     f"{sid} R2 Entry-path: {arg!r} is not a registered alias "
                                     f"on any file"))
                elif _canon(owner, aliases) not in c_must:
                    problems.append(("ERROR", rel,
                                     f"{sid} R3 Entry-path: alias {arg!r} is owned by {owner}, "
                                     f"which is not in Must-surface"))
            elif prefix == "direct":
                if resolve(arg, ids, aliases, roadmap, contrast) is None:
                    problems.append(("ERROR", rel,
                                     f"{sid} R2 Entry-path: direct#{arg} does not resolve to a "
                                     f"file"))
            else:
                problems.append(("ERROR", rel,
                                 f"{sid} R2 Entry-path: unknown doorway prefix {prefix!r} in "
                                 f"{tok!r}"))
        # R4 -- the KB can actually discriminate each asserted false positive
        anchors = sorted(c_must) or sorted(c_mustnot)
        for c in caveats:
            cc = _canon(c, aliases)
            if not anchors:
                problems.append(("ERROR", rel,
                                 f"{sid} R4 Must-caveat: {c} has no anchor (both Must-surface "
                                 f"and Must-not-surface are none) — nothing to discriminate from"))
            elif not any((cc, a) in discriminators or (a, cc) in discriminators for a in anchors):
                problems.append(("ERROR", rel,
                                 f"{sid} R4 Must-caveat: {c} has no distinguished-from edge to "
                                 f"any of {', '.join(anchors)} — the KB cannot discriminate this "
                                 f"false positive"))
        # R5 -- the gate has somewhere real to route to
        if gate != "none":
            routed = False
            for fid in route:
                r = by_id.get(_canon(fid, aliases))
                if r and r["fm"].get("safety") == gate and SAFETY_H.search(r["body"]):
                    routed = True
            if not routed:
                problems.append(("ERROR", rel,
                                 f"{sid} R5 Safety-route: no routed file carries both "
                                 f"'safety: {gate}' and a '## Safety notes' section"))
        # R6 -- per-kind required fields
        if kind not in KINDS:
            problems.append(("ERROR", rel,
                             f"{sid} R6 Kind: illegal kind {kind!r} (expected one of "
                             f"{', '.join(sorted(KINDS))})"))
        for key in ("Kind", "Input", "Rubric", "Trigger"):
            if not f.get(key, "").strip():
                problems.append(("ERROR", rel, f"{sid} R6: missing or empty {key}"))
        if kind == "detection":
            for key, val in (("Entry-path", entry), ("Must-surface", must),
                             ("Must-caveat", caveats)):
                if not val:
                    problems.append(("ERROR", rel,
                                     f"{sid} R6 detection: {key} is empty — a detection scenario "
                                     f"must enter somewhere, name something, and caveat it"))
        elif kind == "look-alike":
            for key, val in (("Must-not-surface", mustnot), ("Must-caveat", caveats)):
                if not val:
                    problems.append(("ERROR", rel,
                                     f"{sid} R6 look-alike: {key} is empty — a look-alike "
                                     f"scenario must rule something out and say what it is"))
        elif kind == "safety":
            if gate == "none":
                problems.append(("ERROR", rel, f"{sid} R6 safety: Safety-gate is none"))
            if not route:
                problems.append(("ERROR", rel, f"{sid} R6 safety: Safety-route names no file"))
        elif kind == "named-construct":
            if not any(_norm(t.partition("#")[0]) in ("alias", "bias-codex") for t in entry):
                problems.append(("ERROR", rel,
                                 f"{sid} R6 named-construct: no alias# or bias-codex# Entry-path "
                                 f"— the name the person arrived with is the doorway"))
        elif kind == "weaponization":
            if _norm(f.get("Refusal", "")) != "required":
                problems.append(("ERROR", rel,
                                 f"{sid} R6 weaponization: Refusal must be 'required'"))
            if must:
                problems.append(("ERROR", rel,
                                 f"{sid} R6 weaponization: Must-surface must be none "
                                 f"(got {', '.join(must)})"))
        elif kind == "third-party":
            if "helping-others" not in c_must:
                problems.append(("ERROR", rel,
                                 f"{sid} R6 third-party: helping-others must be in Must-surface"))
    return _report_eval(problems, scenarios, coverage, declared, rmax, by_kind)


def _report_eval(problems, scenarios, coverage, declared, rmax, by_kind=None):
    errors = [p for p in problems if p[0] == "ERROR"]
    warns = [p for p in problems if p[0] == "WARN"]
    for lvl, rel_path, msg in problems:
        print(f"{lvl:5} {rel_path}: {msg}")
    print(f"\nscenarios: {len(scenarios)} — " +
          (", ".join(f"{k}={v}" for k, v in sorted((by_kind or {}).items())) or "none"))
    print("doorways:  " + ", ".join(f"{p} ({r})" for p, r in sorted(DOORWAYS.items())))
    print("reachable: " + ", ".join(f"{t} {n}/{total}"
                                    for t, (n, total) in sorted(coverage.items())))
    print(f"tiers:     eval declares 0-{declared}, ROADMAP reaches {rmax}")
    print(f"eval: {len(errors)} errors, {len(warns)} warnings")
    print("NOTE: retrieval structure only. Behavioural conformance (escalation ordering, "
          "calibration, refusal, diagnosis creep) is NOT checked here -- run the agent protocol "
          "in meta/agent-evals.md.")
    return 1 if errors else 0


def main():
    cmds = {"validate": cmd_validate, "graph": cmd_graph,
            "matrix": cmd_matrix, "stats": cmd_stats, "eval": cmd_eval}
    if len(sys.argv) != 2 or sys.argv[1] not in cmds:
        print(__doc__)
        return 2
    return cmds[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())

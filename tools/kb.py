#!/usr/bin/env python3
"""Mind Protector KB toolchain (stdlib only).

Commands:
  validate  schema, enums, id=filename, edge/wikilink resolution, section gates
  graph     compile typed edges from frontmatter -> graph/edges.yaml
  matrix    regenerate graph/tactic-mechanism.md and graph/tactic-context.md
  stats     coverage by type/status, edge counts, ROADMAP cross-check

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
ROADMAP_ID = re.compile(r"^- \[[ xX]\] `([a-z0-9-]+)`", re.M)
ROADMAP_CHECKED = re.compile(r"^- \[[xX]\] `([a-z0-9-]+)`", re.M)
GLOSSARY_ID = re.compile(r"^- `([a-z0-9-]+)`", re.M)
FENCED = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")


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
        if fm.get("safety") and "## Safety notes" not in r["body"]:
            problems.append((level, rel, "safety-flagged but no '## Safety notes' section"))
        if status == "complete" and "## Sources" not in r["body"]:
            problems.append(("ERROR", rel, "complete but no '## Sources' section"))
    # alias collisions
    ids, aliases, roadmap, contrast = load_targets(records)
    for r in records:
        for a in r["fm"].get("aliases", []) if isinstance(r["fm"].get("aliases", []), list) else []:
            if a in ids and a != r["fm"].get("id"):
                problems.append(("ERROR", r["rel"], f"alias {a!r} collides with an id"))
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


def main():
    cmds = {"validate": cmd_validate, "graph": cmd_graph,
            "matrix": cmd_matrix, "stats": cmd_stats}
    if len(sys.argv) != 2 or sys.argv[1] not in cmds:
        print(__doc__)
        return 2
    return cmds[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())

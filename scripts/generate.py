#!/usr/bin/env python3
"""Read src/ai.yaml and write rule/{Clash,Stash,Surge,Shadowrocket}/AI.*."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
src = root / "src" / "ai.yaml"


def parse(path: Path):
    title, rules, seen_title = "AI", [], False
    for line in path.read_text().splitlines():
        s = line.strip()
        if s.startswith("# ") and not seen_title:
            title = s[2:]
            seen_title = True
        elif s.startswith("- "):
            rules.append(s[2:])
    return title, rules


def to_list(rules):
    return [r[: -len(",no-resolve")] if r.endswith(",no-resolve") else r for r in rules]


title, rules = parse(src)

for client, fmt in (("Clash", "yaml"), ("Stash", "list"), ("Surge", "list"), ("Shadowrocket", "list")):
    d = root / "rule" / client
    d.mkdir(parents=True, exist_ok=True)
    if fmt == "yaml":
        body = [f"# {title}", "payload:"] + [f"  - {r}" for r in rules]
        (d / "AI.yaml").write_text("\n".join(body) + "\n")
    else:
        (d / "AI.list").write_text("\n".join([f"# {title}"] + to_list(rules)) + "\n")
    print(f"wrote AI.{fmt} -> rule/{client}")

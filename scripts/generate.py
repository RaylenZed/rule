#!/usr/bin/env python3
"""Read src/*.yaml and write rule/{Clash,Stash,Surge,Shadowrocket}."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
src = root / "src"

def parse(path: Path):
    title, rules = path.stem, []
    for line in path.read_text().splitlines():
        s = line.strip()
        if s.startswith("# ") and not rules:
            title = s[2:]
        elif s.startswith("- "):
            rules.append(s[2:])
    return title, rules

def to_list(rules):
    return [r[: -len(",no-resolve")] if r.endswith(",no-resolve") else r for r in rules]

apps = {p.stem: parse(p) for p in sorted(src.glob("*.yaml"))}

for client, fmt in (("Clash", "yaml"), ("Stash", "list"), ("Surge", "list"), ("Shadowrocket", "list")):
    d = root / "rule" / client
    d.mkdir(parents=True, exist_ok=True)
    for name, (title, rules) in apps.items():
        if fmt == "yaml":
            body = [f"# {title}", "payload:"] + [f"  - {r}" for r in rules]
            (d / f"{name}.yaml").write_text("\n".join(body) + "\n")
        else:
            (d / f"{name}.list").write_text("\n".join([f"# {title}"] + to_list(rules)) + "\n")
    print(f"wrote {len(apps)} files -> rule/{client}")

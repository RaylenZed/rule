#!/usr/bin/env python3
"""Read src/ai.yaml and write rule/{Clash,Stash,Surge,Shadowrocket}/AI.*."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
src = root / "src" / "ai.yaml"


def strip_no_resolve(rule: str) -> str:
    suffix = ",no-resolve"
    return rule[: -len(suffix)] if rule.endswith(suffix) else rule


def parse(path: Path):
    header, body, in_body = [], [], False
    for line in path.read_text().splitlines():
        s = line.strip()
        if not in_body:
            if s == "rules:":
                in_body = True
            elif s.startswith("#") or s == "":
                header.append(s)
            continue
        if s == "":
            body.append(("blank", ""))
        elif s.startswith("#"):
            body.append(("comment", s))
        elif s.startswith("- "):
            body.append(("rule", s[2:]))
    return header, body


header, body = parse(src)

for client, fmt in (("Clash", "yaml"), ("Stash", "list"), ("Surge", "list"), ("Shadowrocket", "list")):
    d = root / "rule" / client
    d.mkdir(parents=True, exist_ok=True)
    out = list(header)
    if fmt == "yaml":
        out.append("payload:")
        for kind, value in body:
            if kind == "blank":
                out.append("")
            elif kind == "comment":
                out.append(f"  {value}")
            else:
                out.append(f"  - {value}")
        (d / "AI.yaml").write_text("\n".join(out) + "\n")
    else:
        for kind, value in body:
            if kind == "blank":
                out.append("")
            elif kind == "comment":
                out.append(value)
            else:
                out.append(strip_no_resolve(value))
        (d / "AI.list").write_text("\n".join(out) + "\n")
    print(f"wrote AI.{fmt} -> rule/{client}")

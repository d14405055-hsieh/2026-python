"""U01 easy：字串分割陷阱速記版。"""

from __future__ import annotations

import re


def split_gotchas(line: str) -> dict[str, object]:
    """捕獲分組保留分隔符、以及空白正規化。"""
    fields = re.split(r"(;|,|\s)\s*", line)
    values = fields[::2]
    delimiters = fields[1::2] + [""]
    rebuilt = "".join(v + d for v, d in zip(values, delimiters))
    return {
        "values": values,
        "rebuilt": rebuilt,
        "normalized": re.sub(r"\s+", " ", "  hello     world  ".strip()),
    }


if __name__ == "__main__":
    print(split_gotchas("asdf fjdk; afed, fjek,asdf, foo"))

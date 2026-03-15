from __future__ import annotations

import sys


def solve(text: str) -> str:
    open_quote = True
    out_chars: list[str] = []

    for ch in text:
        if ch == '"':
            if open_quote:
                out_chars.append("``")
            else:
                out_chars.append("''")
            open_quote = not open_quote
        else:
            out_chars.append(ch)

    return "".join(out_chars)


if __name__ == "__main__":
    data = sys.stdin.read()
    print(solve(data), end="")

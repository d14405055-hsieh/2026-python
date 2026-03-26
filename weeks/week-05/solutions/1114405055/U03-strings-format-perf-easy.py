"""U03 easy：字串格式化效能速記版。"""

from __future__ import annotations


class SafeSub(dict):
    """缺失鍵時保留原佔位符，避免 KeyError。"""

    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


def format_perf_easy(parts: list[str]) -> dict[str, object]:
    """只保留最實用重點：join 與 format_map。"""
    joined = "".join(parts)
    sentence = "{name} has {n} messages.".format_map(SafeSub({"name": "Guido"}))
    return {
        "joined_len": len(joined),
        "safe_format": sentence,
        "bytes_first": b"Hello"[0],
    }


if __name__ == "__main__":
    print(format_perf_easy(["a", "b", "c"]))

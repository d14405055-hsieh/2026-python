"""R_02 easy：enumerate/zip 重點版。"""

from __future__ import annotations


def enumerate_zip_easy(names: list[str], scores: list[int]) -> dict[str, object]:
    """用最少語法完成序號與配對。"""
    numbered = list(enumerate(names, 1))
    paired = list(zip(names, scores))
    return {"numbered": numbered, "paired": paired}


if __name__ == "__main__":
    print(enumerate_zip_easy(["Alice", "Bob"], [90, 85]))

"""U07 easy：隨機與安全亂數速記版。"""

from __future__ import annotations

import random
import secrets


def random_easy() -> dict[str, object]:
    """重點：random 可重現，secrets 適合安全場景。"""
    r1 = random.Random(42)
    r2 = random.Random(42)
    seq1 = [r1.randint(1, 10) for _ in range(5)]
    seq2 = [r2.randint(1, 10) for _ in range(5)]
    return {
        "same_seed_same_seq": seq1 == seq2,
        "secure_int": secrets.randbelow(100),
        "secure_hex_len": len(secrets.token_hex(16)),
    }


if __name__ == "__main__":
    print(random_easy())

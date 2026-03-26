"""U07. 隨機種子與安全亂數。"""

from __future__ import annotations

import random
import secrets


def reproducible_sequences(seed: int = 42, count: int = 5) -> tuple[list[int], list[int], bool]:
	"""相同種子會產生相同序列。"""
	rng1 = random.Random(seed)
	rng2 = random.Random(seed)
	seq1 = [rng1.randint(1, 100) for _ in range(count)]
	seq2 = [rng2.randint(1, 100) for _ in range(count)]
	return seq1, seq2, seq1 == seq2


def independent_streams() -> tuple[float, float]:
	"""不同 Random 實例具有獨立狀態。"""
	rng1 = random.Random(1)
	rng2 = random.Random(2)
	return rng1.random(), rng2.random()


def secure_random_samples() -> dict[str, object]:
	"""示範 secrets 模組的安全亂數 API。"""
	return {
		"randbelow": secrets.randbelow(100),
		"token_hex_len": len(secrets.token_hex(16)),
		"token_bytes_len": len(secrets.token_bytes(16)),
	}


if __name__ == "__main__":
	print(reproducible_sequences())
	print(independent_streams())
	print(secure_random_samples())

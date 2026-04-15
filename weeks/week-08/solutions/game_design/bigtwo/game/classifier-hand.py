"""Phase 2: 牌型分類器（含繁體中文註解）。"""

from __future__ import annotations

from collections import Counter
from enum import IntEnum
from typing import Optional

from .models import Card


class CardType(IntEnum):
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    @staticmethod
    def _is_straight(ranks: list[int]) -> bool:
        r = sorted(ranks)
        # 支援 A-2-3-4-5（以 5 當高牌）
        if r == [3, 4, 5, 14, 15]:
            return True
        return all(r[i + 1] - r[i] == 1 for i in range(4))

    @staticmethod
    def _straight_high(ranks: list[int]) -> int:
        r = sorted(ranks)
        return 5 if r == [3, 4, 5, 14, 15] else max(r)

    @staticmethod
    def _is_flush(suits: list[int]) -> bool:
        return len(set(suits)) == 1

    @staticmethod
    def classify(cards: list[Card]) -> Optional[tuple[CardType, int, int]]:
        n = len(cards)
        if n == 0:
            return None
        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        cnt = Counter(ranks)
        high_suit = max(c.suit for c in cards)

        if n == 1:
            c = cards[0]
            return (CardType.SINGLE, c.rank, c.suit)

        if n == 2 and len(cnt) == 1:
            rank = ranks[0]
            return (CardType.PAIR, rank, min(suits))

        if n == 3 and len(cnt) == 1:
            rank = ranks[0]
            return (CardType.TRIPLE, rank, min(suits))

        if n != 5:
            return None

        is_flush = HandClassifier._is_flush(suits)
        is_straight = HandClassifier._is_straight(ranks)

        if is_flush and is_straight:
            return (CardType.STRAIGHT_FLUSH, HandClassifier._straight_high(ranks), high_suit)

        if 4 in cnt.values():
            four_rank = next(k for k, v in cnt.items() if v == 4)
            return (CardType.FOUR_OF_A_KIND, four_rank, high_suit)

        if sorted(cnt.values()) == [2, 3]:
            triple_rank = next(k for k, v in cnt.items() if v == 3)
            return (CardType.FULL_HOUSE, triple_rank, high_suit)

        if is_flush:
            return (CardType.FLUSH, max(ranks), high_suit)

        if is_straight:
            return (CardType.STRAIGHT, HandClassifier._straight_high(ranks), high_suit)

        return None

    @staticmethod
    def compare(play1: list[Card], play2: list[Card]) -> int:
        a = HandClassifier.classify(play1)
        b = HandClassifier.classify(play2)
        if a is None or b is None:
            return 0
        if a[0] != b[0]:
            return 1 if a[0] > b[0] else -1
        if a[1] != b[1]:
            return 1 if a[1] > b[1] else -1
        if a[2] != b[2]:
            return 1 if a[2] > b[2] else -1
        return 0

    @staticmethod
    def can_play(last_play: list[Card] | None, cards: list[Card]) -> bool:
        cur = HandClassifier.classify(cards)
        if cur is None:
            return False
        if last_play is None:
            # 第一手必須含 3♣
            return any(c.rank == 3 and c.suit == 0 for c in cards)
        prev = HandClassifier.classify(last_play)
        if prev is None:
            return False
        if len(last_play) != len(cards):
            return False
        return HandClassifier.compare(cards, last_play) > 0

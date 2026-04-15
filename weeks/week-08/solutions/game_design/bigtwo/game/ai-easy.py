"""Phase 4: AI 策略（含繁體中文註解）。"""

from __future__ import annotations

from .classifier import CardType, HandClassifier
from .models import Card, Hand


class AIStrategy:
    """簡易貪心策略：分數最高者優先。"""

    TYPE_SCORES = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8,
    }
    EMPTY_HAND_BONUS = 10_000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards: list[Card], hand: Hand, is_first: bool = False) -> float:
        info = HandClassifier.classify(cards)
        if info is None:
            return -1
        ctype, rank, _ = info
        remain = len(hand) - len(cards)
        score = AIStrategy.TYPE_SCORES[ctype] * 100 + rank * 10
        if remain == 0:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remain <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS
        score += sum(1 for c in cards if c.suit == 3) * AIStrategy.SPADE_BONUS
        if is_first and not any(c.rank == 3 and c.suit == 0 for c in cards):
            return -1
        return score

    @staticmethod
    def select_best(valid_plays: list[list[Card]], hand: Hand, is_first: bool = False) -> list[Card] | None:
        if not valid_plays:
            return None
        best = max(valid_plays, key=lambda p: AIStrategy.score_play(p, hand, is_first))
        return best

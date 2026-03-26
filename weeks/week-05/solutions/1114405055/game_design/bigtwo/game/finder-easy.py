"""Phase 3: 牌型搜尋器（含繁體中文註解）。"""

from __future__ import annotations

from itertools import combinations

from .classifier import HandClassifier
from .models import Card, Hand


class HandFinder:
    @staticmethod
    def find_singles(hand: Hand) -> list[list[Card]]:
        return [[c] for c in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> list[list[Card]]:
        out: list[list[Card]] = []
        for a, b in combinations(hand, 2):
            if a.rank == b.rank:
                out.append([a, b])
        return out

    @staticmethod
    def find_triples(hand: Hand) -> list[list[Card]]:
        out: list[list[Card]] = []
        for cards in combinations(hand, 3):
            if len({c.rank for c in cards}) == 1:
                out.append(list(cards))
        return out

    @staticmethod
    def find_fives(hand: Hand) -> list[list[Card]]:
        out: list[list[Card]] = []
        for cards in combinations(hand, 5):
            if HandClassifier.classify(list(cards)) is not None:
                out.append(list(cards))
        return out

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: list[Card] | None) -> list[list[Card]]:
        candidates: list[list[Card]] = []
        candidates.extend(HandFinder.find_singles(hand))
        candidates.extend(HandFinder.find_pairs(hand))
        candidates.extend(HandFinder.find_triples(hand))
        candidates.extend(HandFinder.find_fives(hand))
        return [c for c in candidates if HandClassifier.can_play(last_play, c)]

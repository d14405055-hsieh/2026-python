"""Phase 1: 資料模型（含繁體中文註解）。"""

from __future__ import annotations

from dataclasses import dataclass, field
import random
from typing import Iterable

SUITS = ["♣", "♦", "♥", "♠"]
RANK_STR = {
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "T",
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
    15: "2",
}


@dataclass(frozen=True, order=True)
class Card:
    """單張牌：先比 rank，再比 suit。"""

    rank: int
    suit: int

    def __repr__(self) -> str:
        return f"{SUITS[self.suit]}{RANK_STR[self.rank]}"

    def to_sort_key(self) -> tuple[int, int]:
        return self.rank, self.suit


@dataclass
class Deck:
    """52 張撲克牌牌堆。"""

    cards: list[Card] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.cards:
            self.cards = self._create_cards()

    def _create_cards(self) -> list[Card]:
        return [Card(rank, suit) for rank in range(3, 16) for suit in range(4)]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> list[Card]:
        taken = self.cards[:n]
        self.cards = self.cards[n:]
        return taken


class Hand(list[Card]):
    """玩家手牌容器。"""

    def __init__(self, cards: Iterable[Card] | None = None):
        super().__init__(cards or [])

    def sort_desc(self) -> None:
        # 大老二慣例：rank 大到小，若同 rank 再以 suit 大到小
        self.sort(key=lambda c: (c.rank, c.suit), reverse=True)

    def find_3_clubs(self) -> Card | None:
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove_cards(self, cards: Iterable[Card]) -> None:
        for c in cards:
            if c in self:
                self.remove(c)


@dataclass
class Player:
    """玩家資料：可人類或 AI。"""

    name: str
    is_ai: bool = False
    hand: Hand = field(default_factory=Hand)
    score: int = 0

    def take_cards(self, cards: Iterable[Card]) -> None:
        self.hand.extend(cards)
        self.hand.sort_desc()

    def play_cards(self, cards: list[Card]) -> list[Card]:
        self.hand.remove_cards(cards)
        return cards

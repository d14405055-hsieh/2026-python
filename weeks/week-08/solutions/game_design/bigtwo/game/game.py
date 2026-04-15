"""Phase 5: 遊戲流程（含繁體中文註解）。"""

from __future__ import annotations

from dataclasses import dataclass, field

from .ai import AIStrategy
from .classifier import HandClassifier
from .finder import HandFinder
from .models import Card, Deck, Player


@dataclass
class BigTwoGame:
    deck: Deck = field(default_factory=Deck)
    players: list[Player] = field(
        default_factory=lambda: [
            Player("Player", is_ai=False),
            Player("AI-1", is_ai=True),
            Player("AI-2", is_ai=True),
            Player("AI-3", is_ai=True),
        ]
    )
    current_player: int = 0
    last_play: list[Card] | None = None
    pass_count: int = 0
    winner: Player | None = None

    def setup(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        for p in self.players:
            p.hand.clear()
            p.take_cards(self.deck.deal(13))
        for i, p in enumerate(self.players):
            if p.hand.find_3_clubs() is not None:
                self.current_player = i
                break
        self.last_play = None
        self.pass_count = 0
        self.winner = None

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def _is_valid_play(self, cards: list[Card]) -> bool:
        return HandClassifier.can_play(self.last_play, cards)

    def play(self, player: Player, cards: list[Card]) -> bool:
        if player is not self.get_current_player():
            return False
        if not all(c in player.hand for c in cards):
            return False
        if not self._is_valid_play(cards):
            return False
        player.play_cards(cards)
        self.last_play = cards
        self.pass_count = 0
        self.winner = self.check_winner()
        self.next_turn()
        return True

    def pass_(self, player: Player) -> bool:
        if player is not self.get_current_player():
            return False
        self.pass_count += 1
        self.next_turn()
        self.check_round_reset()
        return True

    def next_turn(self) -> None:
        self.current_player = (self.current_player + 1) % 4

    def check_round_reset(self) -> None:
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0

    def check_winner(self) -> Player | None:
        for p in self.players:
            if len(p.hand) == 0:
                return p
        return None

    def is_game_over(self) -> bool:
        return self.winner is not None

    def ai_turn(self) -> bool:
        player = self.get_current_player()
        if not player.is_ai:
            return False
        valid = HandFinder.get_all_valid_plays(player.hand, self.last_play)
        play = AIStrategy.select_best(valid, player.hand, is_first=self.last_play is None)
        if play is None:
            return self.pass_(player)
        return self.play(player, play)

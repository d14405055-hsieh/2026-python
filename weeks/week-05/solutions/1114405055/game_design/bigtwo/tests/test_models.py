"""Phase 1 測試：models（繁體中文註解）。"""

from __future__ import annotations

import unittest

from game.models import Card, Deck, Hand, Player


class TestModels(unittest.TestCase):
    def test_card_repr(self):
        self.assertEqual(repr(Card(14, 3)), "♠A")
        self.assertEqual(repr(Card(3, 0)), "♣3")

    def test_deck(self):
        d = Deck()
        self.assertEqual(len(d.cards), 52)
        self.assertEqual(len(set(d.cards)), 52)

    def test_hand_find_3_clubs(self):
        h = Hand([Card(14, 3), Card(3, 0)])
        self.assertEqual(h.find_3_clubs(), Card(3, 0))

    def test_player_take_play(self):
        p = Player("P")
        cards = [Card(3, 0), Card(4, 0)]
        p.take_cards(cards)
        played = p.play_cards([Card(3, 0)])
        self.assertEqual(len(played), 1)
        self.assertEqual(len(p.hand), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)

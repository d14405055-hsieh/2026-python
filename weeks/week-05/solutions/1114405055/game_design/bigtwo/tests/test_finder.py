"""Phase 3 測試：finder。"""

from __future__ import annotations

import unittest

from game.finder import HandFinder
from game.models import Card, Hand


class TestFinder(unittest.TestCase):
    def test_find_singles_pairs(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        self.assertEqual(len(HandFinder.find_singles(hand)), 3)
        self.assertEqual(len(HandFinder.find_pairs(hand)), 1)

    def test_first_turn_valid(self):
        hand = Hand([Card(3, 0), Card(4, 0), Card(5, 1)])
        plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(plays, [[Card(3, 0)]])


if __name__ == "__main__":
    unittest.main(verbosity=2)

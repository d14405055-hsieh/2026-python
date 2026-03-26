"""Phase 2 測試：classifier。"""

from __future__ import annotations

import unittest

from game.classifier import CardType, HandClassifier
from game.models import Card


class TestClassifier(unittest.TestCase):
    def test_single_pair(self):
        self.assertEqual(HandClassifier.classify([Card(14, 3)]), (CardType.SINGLE, 14, 3))
        self.assertEqual(HandClassifier.classify([Card(14, 3), Card(14, 2)])[0], CardType.PAIR)

    def test_straight_flush(self):
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        self.assertEqual(HandClassifier.classify(cards)[0], CardType.STRAIGHT_FLUSH)

    def test_can_play(self):
        self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)]))
        self.assertFalse(HandClassifier.can_play(None, [Card(14, 3)]))


if __name__ == "__main__":
    unittest.main(verbosity=2)

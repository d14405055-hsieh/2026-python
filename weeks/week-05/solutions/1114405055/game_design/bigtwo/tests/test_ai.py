"""Phase 4 測試：AI 策略。"""

from __future__ import annotations

import unittest

from game.ai import AIStrategy
from game.models import Card, Hand


class TestAI(unittest.TestCase):
    def test_score_and_select(self):
        hand = Hand([Card(3, 0), Card(14, 3), Card(14, 2)])
        single = [Card(3, 0)]
        pair = [Card(14, 3), Card(14, 2)]
        self.assertGreater(AIStrategy.score_play(pair, hand), AIStrategy.score_play(single, hand))
        self.assertEqual(AIStrategy.select_best([single, pair], hand), pair)


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""Phase 5 測試：遊戲流程。"""

from __future__ import annotations

import unittest

from game.game import BigTwoGame


class TestGame(unittest.TestCase):
    def test_setup(self):
        g = BigTwoGame()
        g.setup()
        self.assertEqual(len(g.players), 4)
        self.assertEqual(sum(len(p.hand) for p in g.players), 52)

    def test_pass_and_reset(self):
        g = BigTwoGame()
        g.setup()
        # 模擬三次過牌後會重置回合
        for _ in range(3):
            p = g.get_current_player()
            g.pass_(p)
        self.assertIsNone(g.last_play)


if __name__ == "__main__":
    unittest.main(verbosity=2)

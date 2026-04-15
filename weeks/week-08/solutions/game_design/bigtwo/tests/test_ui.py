"""Phase 6 測試：GUI 簡化介面。"""

from __future__ import annotations

import unittest

from ui.app import BigTwoApp
from ui.input import InputHandler


class TestUI(unittest.TestCase):
    def test_app_init(self):
        app = BigTwoApp()
        self.assertIsNotNone(app.renderer)

    def test_input_toggle(self):
        h = InputHandler()
        h.toggle_select(2)
        self.assertIn(2, h.selected_indices)
        h.toggle_select(2)
        self.assertNotIn(2, h.selected_indices)


if __name__ == "__main__":
    unittest.main(verbosity=2)

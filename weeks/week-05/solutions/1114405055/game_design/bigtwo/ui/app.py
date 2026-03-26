"""Phase 6: GUI 主程式（簡化版）。"""

from __future__ import annotations

from .input import InputHandler
from .render import Renderer


class BigTwoApp:
    """不強制啟動 pygame 視窗，方便在教學環境測試。"""

    def __init__(self):
        self.renderer = Renderer()
        self.input_handler = InputHandler()

    def run_once(self) -> bool:
        """回傳是否具備 pygame 執行條件。"""
        return self.renderer.ready

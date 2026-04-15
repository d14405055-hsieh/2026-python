"""Phase 6: GUI 渲染器（簡化版，含繁體中文註解）。"""

from __future__ import annotations

try:
    import pygame
except Exception:  # pragma: no cover
    pygame = None


class Renderer:
    """最小可用渲染器；若環境無 pygame，測試會用 mock。"""

    CARD_WIDTH = 60
    CARD_HEIGHT = 90

    def __init__(self):
        self.ready = pygame is not None

    def card_rect(self, index: int, x: int, y: int):
        if pygame is None:
            return (x + index * 20, y, self.CARD_WIDTH, self.CARD_HEIGHT)
        return pygame.Rect(x + index * 20, y, self.CARD_WIDTH, self.CARD_HEIGHT)

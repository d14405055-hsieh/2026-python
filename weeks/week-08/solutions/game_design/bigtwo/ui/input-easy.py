"""Phase 6: GUI 輸入處理（簡化版）。"""

from __future__ import annotations


class InputHandler:
    """簡化輸入：保留選牌索引，供測試驗證。"""

    def __init__(self):
        self.selected_indices: list[int] = []

    def toggle_select(self, index: int) -> None:
        if index in self.selected_indices:
            self.selected_indices.remove(index)
        else:
            self.selected_indices.append(index)

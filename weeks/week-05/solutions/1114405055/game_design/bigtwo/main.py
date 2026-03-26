"""bigtwo 入口檔。"""

from __future__ import annotations

from ui.app import BigTwoApp


if __name__ == "__main__":
    app = BigTwoApp()
    print("pygame ready:", app.run_once())

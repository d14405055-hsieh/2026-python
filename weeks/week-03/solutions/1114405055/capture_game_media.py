from __future__ import annotations

import os
from pathlib import Path

# Use SDL dummy driver so media can be generated automatically in any environment.
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame
from PIL import Image

from robot_game import (
    ASSETS_DIR,
    BG,
    GRID_FILL,
    GRID_LINE,
    PANEL,
    SCENT,
    SUBTEXT,
    TEXT,
    TRACK,
    Game,
    draw_robot,
    draw_text,
    grid_to_screen,
)


def render_frame(
    screen: pygame.Surface,
    game: Game,
    font: pygame.font.Font,
    small: pygame.font.Font,
    left: int,
    top: int,
    cell: int,
    panel_x: int,
) -> None:
    state = game.active_state()

    screen.fill(BG)
    pygame.draw.rect(screen, PANEL, (20, 20, 740, 680), border_radius=14)
    pygame.draw.rect(screen, PANEL, (770, 20, 310, 680), border_radius=14)

    for gy in range(game.height + 1):
        for gx in range(game.width + 1):
            x = left + gx * cell
            y = top + gy * cell
            pygame.draw.rect(screen, GRID_FILL, (x, y, cell, cell))
            pygame.draw.rect(screen, GRID_LINE, (x, y, cell, cell), 1)

    if len(game.current_track) >= 2:
        pts = [
            grid_to_screen(s.x, s.y, left, top, cell, game.height)
            for s in game.current_track
        ]
        pygame.draw.lines(screen, TRACK, False, pts, 3)

    for sx, sy, sd in game.scents:
        px, py = grid_to_screen(sx, sy, left, top, cell, game.height)
        pygame.draw.circle(screen, SCENT, (px, py), 10)
        draw_text(screen, sd, (px - 7, py + 14), small, SCENT)

    draw_robot(screen, state, left, top, cell, game.height)

    draw_text(screen, "UVA118 星圖巡航", (panel_x, 44), font)
    draw_text(screen, f"狀態: ({state.x},{state.y},{state.direction})", (panel_x, 82), small)
    draw_text(screen, f"LOST: {state.lost}", (panel_x, 108), small)
    draw_text(screen, f"Scent 數量: {len(game.scents)}", (panel_x, 134), small)
    draw_text(screen, "操作鍵", (panel_x, 218), font)

    controls = [
        "L/R/F: 左轉/右轉/前進",
        "N: 新機器人",
        "C: 清除 scent",
        "P: 回放開關",
        "D: 自動演示",
        "M: 匯出 matrix_snapshot.txt",
        "G: 匯出 replay.txt",
        "S: 儲存 gameplay.png",
        "Q / ESC: 離開",
    ]
    yy = 250
    for line in controls:
        draw_text(screen, line, (panel_x, yy), small, SUBTEXT)
        yy += 24

    draw_text(screen, "最近事件", (panel_x, 500), font)
    for i, msg in enumerate(game.events[-7:]):
        draw_text(screen, "- " + msg, (panel_x, 532 + i * 22), small, SUBTEXT)


def surface_to_image(surface: pygame.Surface) -> Image.Image:
    raw = pygame.image.tostring(surface, "RGB")
    return Image.frombytes("RGB", surface.get_size(), raw)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((1100, 720))

    font = pygame.font.SysFont("Consolas", 22)
    small = pygame.font.SysFont("Consolas", 18)

    game = Game()
    left = 40
    top = 70
    cell = 120
    panel_x = 790

    commands = ["F", "F", "F", "F", "N", "F", "F", "F", "F", "R", "F", "F"]
    frames: list[Image.Image] = []

    render_frame(screen, game, font, small, left, top, cell, panel_x)
    frames.append(surface_to_image(screen))

    for cmd in commands:
        if cmd == "N":
            game.reset_robot()
        else:
            game.apply(cmd)
        render_frame(screen, game, font, small, left, top, cell, panel_x)
        frames.append(surface_to_image(screen))

    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    screenshot_path = ASSETS_DIR / "gameplay.png"
    gif_path = ASSETS_DIR / "gameplay.gif"

    frames[-1].save(screenshot_path)
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=300,
        loop=0,
    )

    game.export_matrix_snapshot()
    game.export_replay_log()

    pygame.quit()
    print(f"saved: {screenshot_path}")
    print(f"saved: {gif_path}")


if __name__ == "__main__":
    main()

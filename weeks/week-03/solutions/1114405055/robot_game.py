from __future__ import annotations

from pathlib import Path

import pygame

from robot_core import RobotState, run_step

ASSETS_DIR = Path(__file__).parent / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

BG = (10, 14, 28)
PANEL = (18, 25, 46)
GRID_LINE = (52, 66, 102)
GRID_FILL = (14, 20, 38)
ROBOT = (80, 220, 255)
ROBOT_LOST = (255, 96, 96)
SCENT = (255, 184, 77)
TRACK = (120, 130, 220)
TEXT = (228, 236, 255)
SUBTEXT = (160, 174, 208)

ARROW_VEC = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}


class Game:
    def __init__(self, width: int = 5, height: int = 3) -> None:
        self.width = width
        self.height = height
        self.scents: set[tuple[int, int, str]] = set()
        self.robot = RobotState(0, 0, "N", False)
        self.command_history: list[str] = []
        self.events: list[str] = ["遊戲開始"]
        self.current_track: list[RobotState] = [self.robot]

        self.replay_mode = False
        self.replay_idx = 0
        self.replay_tick_ms = 260
        self.last_replay_tick = 0

        self.demo_mode = False
        self.demo_tick_ms = 360
        self.last_demo_tick = 0
        self.demo_commands: list[str] = []

    def active_state(self) -> RobotState:
        if self.replay_mode and self.current_track:
            return self.current_track[self.replay_idx]
        return self.robot

    def reset_robot(self) -> None:
        self.robot = RobotState(0, 0, "N", False)
        self.command_history.clear()
        self.current_track = [self.robot]
        self.replay_mode = False
        self.replay_idx = 0
        self.events.append("部署新機器人：位置 (0,0) 朝向 N")

    def clear_scents(self) -> None:
        self.scents.clear()
        self.events.append("已清除全部 scent")

    def apply(self, command: str) -> None:
        step = run_step(self.robot, command, self.width, self.height, self.scents)
        self.robot = step.state
        self.command_history.append(command)
        self.current_track.append(self.robot)
        self.replay_mode = False

        if step.event == "LOST":
            self.events.append(
                f"{command}: LOST 於 ({self.robot.x},{self.robot.y},{self.robot.direction})"
            )
        elif step.event == "SCENT_BLOCK":
            self.events.append(f"{command}: scent 保護，忽略危險前進")
        else:
            self.events.append(
                f"{command}: {step.event} -> ({self.robot.x},{self.robot.y},{self.robot.direction})"
            )

    def start_demo(self) -> None:
        # Robot 1 gets LOST on north edge, then Robot 2 is protected by scent.
        self.reset_robot()
        self.clear_scents()
        self.demo_commands = ["F", "F", "F", "F", "N", "F", "F", "F", "F", "R", "F", "F"]
        self.demo_mode = True
        self.last_demo_tick = pygame.time.get_ticks()
        self.events.append("啟動自動演示")

    def tick_demo(self) -> None:
        if not self.demo_mode:
            return
        now = pygame.time.get_ticks()
        if now - self.last_demo_tick < self.demo_tick_ms:
            return
        self.last_demo_tick = now

        if not self.demo_commands:
            self.demo_mode = False
            self.events.append("自動演示完成")
            return

        cmd = self.demo_commands.pop(0)
        if cmd == "N":
            self.reset_robot()
        else:
            self.apply(cmd)

    def toggle_replay(self) -> None:
        if len(self.current_track) <= 1:
            self.events.append("尚無路徑可回放")
            return
        self.replay_mode = not self.replay_mode
        self.replay_idx = 0
        self.last_replay_tick = pygame.time.get_ticks()
        self.events.append("開啟回放模式" if self.replay_mode else "關閉回放模式")

    def tick_replay(self) -> None:
        if not self.replay_mode:
            return
        now = pygame.time.get_ticks()
        if now - self.last_replay_tick < self.replay_tick_ms:
            return
        self.last_replay_tick = now
        self.replay_idx += 1
        if self.replay_idx >= len(self.current_track):
            self.replay_idx = 0

    def matrix_10x10(self) -> list[str]:
        marker = {"N": "^", "E": ">", "S": "v", "W": "<"}
        state = self.active_state()
        grid = [["." for _ in range(10)] for _ in range(10)]

        for sx, sy, _ in self.scents:
            if 0 <= sx < 10 and 0 <= sy < 10:
                grid[sy][sx] = "*"

        if 0 <= state.x < 10 and 0 <= state.y < 10:
            grid[state.y][state.x] = "X" if state.lost else marker[state.direction]

        return ["".join(row) for row in reversed(grid)]

    def export_matrix_snapshot(self) -> Path:
        out = ASSETS_DIR / "matrix_snapshot.txt"
        with out.open("w", encoding="utf-8") as f:
            f.write("10x10 Matrix Snapshot\n")
            f.write(
                f"Robot=({self.robot.x},{self.robot.y},{self.robot.direction}) lost={self.robot.lost}\n"
            )
            f.write(f"Scents={sorted(self.scents)}\n\n")
            for row in self.matrix_10x10():
                f.write(row + "\n")
        self.events.append(f"已輸出: {out.name}")
        return out

    def export_replay_log(self) -> Path:
        out = ASSETS_DIR / "replay.txt"
        with out.open("w", encoding="utf-8") as f:
            f.write("Replay Track\n")
            for i, s in enumerate(self.current_track):
                f.write(f"{i:02d}: ({s.x},{s.y},{s.direction}) lost={s.lost}\n")
        self.events.append(f"已輸出: {out.name}")
        return out


def grid_to_screen(x: int, y: int, left: int, top: int, cell: int, h: int) -> tuple[int, int]:
    px = left + x * cell + cell // 2
    py = top + (h - y) * cell + cell // 2
    return px, py


def draw_robot(
    screen: pygame.Surface,
    state: RobotState,
    left: int,
    top: int,
    cell: int,
    h: int,
) -> None:
    cx, cy = grid_to_screen(state.x, state.y, left, top, cell, h)
    if state.lost:
        pygame.draw.circle(screen, ROBOT_LOST, (cx, cy), cell // 3)
        pygame.draw.line(screen, (255, 220, 220), (cx - 10, cy - 10), (cx + 10, cy + 10), 3)
        pygame.draw.line(screen, (255, 220, 220), (cx + 10, cy - 10), (cx - 10, cy + 10), 3)
        return

    vx, vy = ARROW_VEC[state.direction]
    tip = (cx + vx * (cell // 3), cy + vy * (cell // 3))
    left_pt = (cx + vy * (cell // 4), cy - vx * (cell // 4))
    right_pt = (cx - vy * (cell // 4), cy + vx * (cell // 4))
    pygame.draw.polygon(screen, ROBOT, [tip, left_pt, right_pt])


def draw_text(
    surface: pygame.Surface,
    text: str,
    pos: tuple[int, int],
    font: pygame.font.Font,
    color: tuple[int, int, int] = TEXT,
) -> None:
    surface.blit(font.render(text, True, color), pos)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((1100, 720))
    pygame.display.set_caption("UVA118 星圖巡航")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Consolas", 22)
    small = pygame.font.SysFont("Consolas", 18)

    game = Game()

    left = 40
    top = 70
    cell = 120
    panel_x = 790

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False
                elif event.key == pygame.K_l:
                    game.apply("L")
                elif event.key == pygame.K_r:
                    game.apply("R")
                elif event.key == pygame.K_f:
                    game.apply("F")
                elif event.key == pygame.K_n:
                    game.reset_robot()
                elif event.key == pygame.K_c:
                    game.clear_scents()
                elif event.key == pygame.K_p:
                    game.toggle_replay()
                elif event.key == pygame.K_d:
                    game.start_demo()
                elif event.key == pygame.K_m:
                    game.export_matrix_snapshot()
                elif event.key == pygame.K_g:
                    game.export_replay_log()
                elif event.key == pygame.K_s:
                    shot = ASSETS_DIR / "gameplay.png"
                    pygame.image.save(screen, shot)
                    game.events.append(f"已輸出: {shot.name}")

        game.tick_demo()
        game.tick_replay()
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
        draw_text(screen, f"回放模式: {game.replay_mode}", (panel_x, 160), small)
        draw_text(screen, f"演示模式: {game.demo_mode}", (panel_x, 186), small)

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

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

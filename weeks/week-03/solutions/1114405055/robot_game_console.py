from __future__ import annotations

from pathlib import Path

from robot_core import RobotState, run_step

ASSETS_DIR = Path(__file__).parent / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

ARROW = {"N": "^", "E": ">", "S": "v", "W": "<"}


class Game:
    def __init__(self, width: int = 5, height: int = 3) -> None:
        self.width = width
        self.height = height
        self.scents: set[tuple[int, int, str]] = set()
        self.robot = RobotState(0, 0, "N", False)
        self.command_history: list[str] = []
        self.events: list[str] = []
        self.current_track: list[RobotState] = [self.robot]

    def reset_robot(self) -> None:
        self.robot = RobotState(0, 0, "N", False)
        self.command_history.clear()
        self.events.append("部署新機器人：位置 (0,0) 朝向 N")
        self.current_track = [self.robot]

    def clear_scents(self) -> None:
        self.scents.clear()
        self.events.append("已清除全部 scent")

    def apply(self, command: str) -> None:
        command = command.upper()
        step = run_step(self.robot, command, self.width, self.height, self.scents)
        self.robot = step.state
        self.command_history.append(command)
        self.current_track.append(self.robot)

        if step.event == "LOST":
            self.events.append(
                f"指令 {command}: LOST 於 ({self.robot.x},{self.robot.y},{self.robot.direction})"
            )
        elif step.event == "SCENT_BLOCK":
            self.events.append(f"指令 {command}: 觸發 scent 保護，忽略危險前進")
        else:
            self.events.append(
                f"指令 {command}: {step.event} -> ({self.robot.x},{self.robot.y},{self.robot.direction})"
            )

    def matrix_10x10(self) -> list[str]:
        grid = [["." for _ in range(10)] for _ in range(10)]

        for sx, sy, _ in self.scents:
            if 0 <= sx < 10 and 0 <= sy < 10:
                grid[sy][sx] = "*"

        if 0 <= self.robot.x < 10 and 0 <= self.robot.y < 10:
            grid[self.robot.y][self.robot.x] = "X" if self.robot.lost else ARROW[self.robot.direction]

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
        return out

    def export_replay_log(self) -> Path:
        out = ASSETS_DIR / "replay.txt"
        with out.open("w", encoding="utf-8") as f:
            f.write("Replay Track\n")
            for i, s in enumerate(self.current_track):
                f.write(f"{i:02d}: ({s.x},{s.y},{s.direction}) lost={s.lost}\n")
        return out

    def render(self) -> None:
        print("\n" + "=" * 56)
        print("UVA118 星圖巡航（Console 版）")
        print("操作: L/R/F=移動, N=新機器人, C=清 scent, P=回放, M=輸出矩陣, G=輸出軌跡, Q=離開")
        print(f"地圖範圍: (0..{self.width}, 0..{self.height})")
        print("-" * 56)

        for y in range(self.height, -1, -1):
            cells = []
            for x in range(0, self.width + 1):
                char = "."
                for sx, sy, _ in self.scents:
                    if sx == x and sy == y:
                        char = "*"
                if self.robot.x == x and self.robot.y == y:
                    char = "X" if self.robot.lost else ARROW[self.robot.direction]
                cells.append(char)
            print(f"y={y}  " + " ".join(cells))

        print("     " + " ".join(f"{x}" for x in range(0, self.width + 1)))
        print(f"狀態: ({self.robot.x},{self.robot.y},{self.robot.direction}) lost={self.robot.lost}")
        print("歷史: " + (" ".join(self.command_history[-12:]) if self.command_history else "(空)"))
        print("最近事件:")
        for msg in self.events[-4:]:
            print("- " + msg)


def replay(track: list[RobotState]) -> None:
    print("\n--- Replay ---")
    for i, state in enumerate(track):
        print(f"step {i:02d}: ({state.x},{state.y},{state.direction}) lost={state.lost}")


def main() -> None:
    game = Game()
    game.events.append("遊戲開始")

    while True:
        game.render()
        cmd = input("輸入指令: ").strip().upper()

        if cmd == "Q":
            print("離開遊戲，歡迎再來。")
            return
        if cmd == "N":
            game.reset_robot()
            continue
        if cmd == "C":
            game.clear_scents()
            continue
        if cmd == "P":
            replay(game.current_track)
            input("按 Enter 返回遊戲...")
            continue
        if cmd == "M":
            path = game.export_matrix_snapshot()
            print(f"已輸出: {path}")
            input("按 Enter 返回遊戲...")
            continue
        if cmd == "G":
            path = game.export_replay_log()
            print(f"已輸出: {path}")
            input("按 Enter 返回遊戲...")
            continue

        if cmd in {"L", "R", "F"}:
            try:
                game.apply(cmd)
            except ValueError as exc:
                game.events.append(str(exc))
            continue

        game.events.append(f"未知指令: {cmd}")


if __name__ == "__main__":
    main()

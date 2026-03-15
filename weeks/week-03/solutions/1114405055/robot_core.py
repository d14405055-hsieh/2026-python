from __future__ import annotations

from dataclasses import dataclass

Direction = str
Scent = tuple[int, int, Direction]

DIRECTIONS: tuple[Direction, ...] = ("N", "E", "S", "W")
MOVE_DELTAS: dict[Direction, tuple[int, int]] = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}
VALID_COMMANDS = {"L", "R", "F"}


@dataclass(frozen=True)
class RobotState:
    x: int
    y: int
    direction: Direction
    lost: bool = False


@dataclass(frozen=True)
class StepResult:
    state: RobotState
    event: str


def turn_left(direction: Direction) -> Direction:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: Direction) -> Direction:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def run_step(
    state: RobotState,
    command: str,
    width: int,
    height: int,
    scents: set[Scent],
) -> StepResult:
    if command not in VALID_COMMANDS:
        raise ValueError(f"Invalid command: {command}")

    if state.lost:
        return StepResult(state=state, event="NOOP_LOST")

    if command == "L":
        return StepResult(
            state=RobotState(state.x, state.y, turn_left(state.direction), False),
            event="TURN",
        )

    if command == "R":
        return StepResult(
            state=RobotState(state.x, state.y, turn_right(state.direction), False),
            event="TURN",
        )

    dx, dy = MOVE_DELTAS[state.direction]
    nx, ny = state.x + dx, state.y + dy

    if 0 <= nx <= width and 0 <= ny <= height:
        return StepResult(state=RobotState(nx, ny, state.direction, False), event="MOVE")

    scent_key = (state.x, state.y, state.direction)
    if scent_key in scents:
        return StepResult(state=state, event="SCENT_BLOCK")

    scents.add(scent_key)
    return StepResult(state=RobotState(state.x, state.y, state.direction, True), event="LOST")

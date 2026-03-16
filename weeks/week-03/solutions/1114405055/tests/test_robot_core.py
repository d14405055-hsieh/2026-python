from robot_core import RobotState, run_step, turn_left, turn_right


def test_turn_left_and_right_cycle() -> None:
    assert turn_left("N") == "W"
    assert turn_left("W") == "S"
    assert turn_right("N") == "E"
    assert turn_right("W") == "N"


def test_forward_move_inside_grid() -> None:
    scents: set[tuple[int, int, str]] = set()
    state = RobotState(0, 0, "N", False)

    step = run_step(state, "F", width=5, height=3, scents=scents)

    assert step.event == "MOVE"
    assert step.state == RobotState(0, 1, "N", False)
    assert scents == set()


def test_lost_when_forward_out_of_grid_without_scent() -> None:
    scents: set[tuple[int, int, str]] = set()
    state = RobotState(0, 3, "N", False)

    step = run_step(state, "F", width=5, height=3, scents=scents)

    assert step.event == "LOST"
    assert step.state == RobotState(0, 3, "N", True)
    assert scents == {(0, 3, "N")}


def test_lost_robot_ignores_follow_up_commands() -> None:
    scents: set[tuple[int, int, str]] = set()
    state = RobotState(2, 2, "E", True)

    step = run_step(state, "F", width=5, height=3, scents=scents)

    assert step.event == "NOOP_LOST"
    assert step.state == state


def test_invalid_command_raises_value_error() -> None:
    scents: set[tuple[int, int, str]] = set()
    state = RobotState(0, 0, "N", False)

    try:
        run_step(state, "X", width=5, height=3, scents=scents)
        assert False, "Expected ValueError for invalid command"
    except ValueError as exc:
        assert "Invalid command" in str(exc)

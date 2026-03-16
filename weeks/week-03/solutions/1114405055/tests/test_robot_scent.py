from robot_core import RobotState, run_step


def test_second_robot_is_blocked_by_existing_scent() -> None:
    scents: set[tuple[int, int, str]] = set()

    # Robot 1 gets lost and leaves scent at (0,3,N).
    robot1 = RobotState(0, 3, "N", False)
    first = run_step(robot1, "F", width=5, height=3, scents=scents)
    assert first.event == "LOST"
    assert first.state.lost is True
    assert scents == {(0, 3, "N")}

    # Robot 2 attempts the same dangerous step and is protected by scent.
    robot2 = RobotState(0, 3, "N", False)
    second = run_step(robot2, "F", width=5, height=3, scents=scents)
    assert second.event == "SCENT_BLOCK"
    assert second.state == robot2
    assert scents == {(0, 3, "N")}


def test_scent_is_direction_specific() -> None:
    scents: set[tuple[int, int, str]] = {(0, 3, "N")}

    # Different direction at same cell should not be blocked by N scent.
    robot = RobotState(0, 3, "E", False)
    step = run_step(robot, "F", width=5, height=3, scents=scents)

    assert step.event == "MOVE"
    assert step.state == RobotState(1, 3, "E", False)


def test_new_lost_direction_adds_another_scent() -> None:
    scents: set[tuple[int, int, str]] = {(0, 3, "N")}

    # Out-of-bound from east edge facing east creates a separate scent key.
    robot = RobotState(5, 3, "E", False)
    step = run_step(robot, "F", width=5, height=3, scents=scents)

    assert step.event == "LOST"
    assert step.state == RobotState(5, 3, "E", True)
    assert scents == {(0, 3, "N"), (5, 3, "E")}

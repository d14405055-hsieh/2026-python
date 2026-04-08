import subprocess


def run_case(inp: str) -> str:
    p = subprocess.run(
        ["python", "solve_10170.py"],
        input=inp,
        text=True,
        capture_output=True,
        check=True,
    )
    return p.stdout.strip()


def test_case_1():
    assert run_case("1 3\n") == "2"


def test_case_2():
    assert run_case("3 14\n") == "6"

import subprocess


def run_case(inp: str) -> str:
    p = subprocess.run(
        ["python", "solve_10093.py"],
        input=inp,
        text=True,
        capture_output=True,
        check=True,
    )
    return p.stdout.strip()


def test_case_1():
    inp = "1 1\nP\n"
    assert run_case(inp) == "1"


def test_case_2():
    inp = "2 3\nPPP\nPPP\n"
    assert run_case(inp) == "2"

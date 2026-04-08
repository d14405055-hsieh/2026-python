import subprocess


def run_case(inp: str) -> str:
    p = subprocess.run(
        ["python", "solve_10101.py"],
        input=inp,
        text=True,
        capture_output=True,
        check=True,
    )
    return p.stdout.strip()


def test_case_has_solution():
    out = run_case("1+1=3#")
    assert out.endswith("#")
    assert out != "No"


def test_case_no_solution():
    out = run_case("1=1#")
    assert out == "No"

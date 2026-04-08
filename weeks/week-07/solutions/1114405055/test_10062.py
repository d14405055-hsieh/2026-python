import subprocess
import textwrap


def run_case(inp: str) -> str:
    p = subprocess.run(
        ["python", "solve_10062.py"],
        input=inp,
        text=True,
        capture_output=True,
        check=True,
    )
    return p.stdout.strip()


def test_case_1():
    inp = textwrap.dedent(
        """\
        5
        1
        1
        3
        2
        """
    )
    assert run_case(inp) == "1\n4\n2\n5\n3"


def test_case_2():
    inp = textwrap.dedent(
        """\
        4
        1
        2
        3
        """
    )
    assert run_case(inp) == "1\n2\n3\n4"

import subprocess


def run_case(inp: str) -> str:
    p = subprocess.run(
        ["python", "solve_10071.py"],
        input=inp,
        text=True,
        capture_output=True,
        check=True,
    )
    return p.stdout.strip()


def brute(nums):
    ans = 0
    for a in nums:
        for b in nums:
            for c in nums:
                for d in nums:
                    for e in nums:
                        for f in nums:
                            if a + b + c + d + e == f:
                                ans += 1
    return ans


def test_case_1():
    nums = [1, 2]
    inp = "2\n1\n2\n"
    assert run_case(inp) == str(brute(nums))


def test_case_2():
    nums = [-1, 0, 1]
    inp = "3\n-1\n0\n1\n"
    assert run_case(inp) == str(brute(nums))

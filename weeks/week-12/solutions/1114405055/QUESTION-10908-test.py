# QUESTION-10908 Test Suite
import subprocess
import sys

def run_test(input_data):
    """運行測試並返回輸出"""
    process = subprocess.Popen(
        [sys.executable, 'QUESTION-10908-manual.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=input_data)
    return stdout.strip()

# 測試案例
test_input = """1
7 10 4
abbbaaaaaa
abbbaaaaaa
abbbaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
5 2"""

expected_output = """7 10 4
3
1
5
1"""

print("=" * 50)
print("QUESTION-10908 — Largest Square Tests")
print("=" * 50)

print(f"\nInput:\n{test_input}")
print(f"\nExpected Output:\n{expected_output}")

actual = run_test(test_input)
print(f"\nActual Output:\n{actual}")

if actual == expected_output:
    print("\nStatus: PASS ✓")
else:
    print("\nStatus: FAIL ✗")
    print("\nDifference:")
    exp_lines = expected_output.split('\n')
    act_lines = actual.split('\n')
    for i, (exp, act) in enumerate(zip(exp_lines, act_lines)):
        if exp != act:
            print(f"  Line {i+1}: Expected '{exp}', Got '{act}'")

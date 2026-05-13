# QUESTION-10931 Test Suite
import subprocess
import sys

def run_test(input_data):
    """運行測試並返回輸出"""
    process = subprocess.Popen(
        [sys.executable, 'QUESTION-10931-manual.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=input_data)
    return stdout.strip()

# 測試案例
test_input = """1
2
10
21
0"""

expected_output = """The parity of 1 is 1 (mod 2).
The parity of 10 is 1 (mod 2).
The parity of 1010 is 2 (mod 2).
The parity of 10101 is 3 (mod 2)."""

print("=" * 50)
print("QUESTION-10931 — Parity Tests")
print("=" * 50)

print(f"\nTest Input:")
for line in test_input.split('\n'):
    if line.strip() and line.strip() != '0':
        print(f"  {line.strip()}")

print(f"\nExpected Output:")
print(expected_output)

actual = run_test(test_input)
print(f"\nActual Output:")
print(actual)

if actual == expected_output:
    print("\nStatus: PASS ✓")
else:
    print("\nStatus: FAIL ✗")
    print("\nLine-by-line Comparison:")
    exp_lines = expected_output.split('\n')
    act_lines = actual.split('\n')
    for i, (exp, act) in enumerate(zip(exp_lines, act_lines)):
        status = "✓" if exp == act else "✗"
        print(f"  {status} Line {i+1}:")
        if exp != act:
            print(f"      Expected: {exp}")
            print(f"      Actual:   {act}")

print("\n" + "=" * 50)

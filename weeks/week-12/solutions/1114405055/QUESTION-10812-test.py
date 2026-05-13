# QUESTION-10812 Test Suite
import subprocess
import sys

def run_test(input_data, expected_output):
    """運行測試並比較輸出"""
    process = subprocess.Popen(
        [sys.executable, 'QUESTION-10812-manual.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=input_data)
    actual_output = stdout.strip()
    expected = expected_output.strip()
    
    if actual_output == expected:
        return True, actual_output
    else:
        return False, actual_output

# 測試案例
test_cases = [
    {
        "input": "2\n40 20\n20 40",
        "expected": "30 10\nimpossible",
        "name": "Test 1: Basic Cases"
    },
    {
        "input": "1\n10 10",
        "expected": "10 0",
        "name": "Test 2: Equal Sum and Diff"
    },
    {
        "input": "1\n0 0",
        "expected": "0 0",
        "name": "Test 3: Both Zero"
    },
]

print("=" * 50)
print("QUESTION-10812 — Beat the Spread! Tests")
print("=" * 50)

passed = 0
failed = 0

for test in test_cases:
    success, actual = run_test(test["input"], test["expected"])
    status = "PASS ✓" if success else "FAIL ✗"
    
    print(f"\n{test['name']}")
    print(f"Status: {status}")
    print(f"Input:\n{test['input']}")
    print(f"Expected:\n{test['expected']}")
    print(f"Actual:\n{actual}")
    
    if success:
        passed += 1
    else:
        failed += 1

print("\n" + "=" * 50)
print(f"Results: {passed} Passed, {failed} Failed")
print("=" * 50)

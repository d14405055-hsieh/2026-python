# QUESTION-10929 Test Suite
import subprocess
import sys

def run_test(input_data):
    """運行測試並返回輸出"""
    process = subprocess.Popen(
        [sys.executable, 'QUESTION-10929-manual.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=input_data)
    return stdout.strip()

# 測試案例
test_cases = [
    {
        "name": "Test 1: 121 (multiple of 11)",
        "input": "121\n0",
        "expected": "121 is a multiple of 11."
    },
    {
        "name": "Test 2: 1111 (multiple of 11)",
        "input": "1111\n0",
        "expected": "1111 is a multiple of 11."
    },
    {
        "name": "Test 3: 123 (not multiple of 11)",
        "input": "123\n0",
        "expected": "123 is not a multiple of 11."
    },
    {
        "name": "Test 4: Large number",
        "input": "10000000000000000001\n0",
        "expected": "10000000000000000001 is a multiple of 11."
    },
]

print("=" * 50)
print("QUESTION-10929 — Multiple of 11 Tests")
print("=" * 50)

passed = 0
failed = 0

for test in test_cases:
    print(f"\n{test['name']}")
    print(f"Input: {test['input'].split(chr(10))[0]}")
    
    actual = run_test(test['input'])
    print(f"Expected: {test['expected']}")
    print(f"Actual:   {actual}")
    
    if actual == test['expected']:
        print("Status: PASS ✓")
        passed += 1
    else:
        print("Status: FAIL ✗")
        failed += 1

print("\n" + "=" * 50)
print(f"Results: {passed} Passed, {failed} Failed")
print("=" * 50)

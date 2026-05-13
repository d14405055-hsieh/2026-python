# QUESTION-10922 Test Suite
import subprocess
import sys

def run_test(input_data):
    """運行測試並返回輸出"""
    process = subprocess.Popen(
        [sys.executable, 'QUESTION-10922-manual.py'],
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
        "name": "Test 1: 9 is multiple of 9",
        "input": "9\n0",
        "expected_contains": "9-degree"
    },
    {
        "name": "Test 2: 18 is multiple of 9",
        "input": "18\n0",
        "expected_contains": "9-degree"
    },
    {
        "name": "Test 3: 10 is not multiple of 9",
        "input": "10\n0",
        "expected_contains": "not a multiple of 9"
    },
    {
        "name": "Test 4: Large number 123456789",
        "input": "123456789\n0",
        "expected_contains": "9-degree"
    },
]

print("=" * 50)
print("QUESTION-10922 — 2 the 9s Tests")
print("=" * 50)

for test in test_cases:
    print(f"\n{test['name']}")
    print(f"Input: {test['input'].split(chr(10))[0]}")
    
    actual = run_test(test['input'])
    print(f"Output: {actual}")
    
    if test['expected_contains'] in actual:
        print("Status: PASS ✓")
    else:
        print(f"Status: FAIL ✗ (Expected to contain '{test['expected_contains']}')")

print("\n" + "=" * 50)

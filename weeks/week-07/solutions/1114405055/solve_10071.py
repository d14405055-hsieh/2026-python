import sys
from collections import defaultdict


def main():
    arr = sys.stdin.read().strip().split()
    if not arr:
        return
    n = int(arr[0])
    nums = list(map(int, arr[1:1 + n]))

    c3 = defaultdict(int)
    for x in nums:
        for y in nums:
            for z in nums:
                c3[x + y + z] += 1

    total = 0
    for d in nums:
        for e in nums:
            for f in nums:
                total += c3[f - d - e]
    print(total)


if __name__ == "__main__":
    main()

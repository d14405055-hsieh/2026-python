"""10055（依題目敘述：函數增減性查詢）手打版"""

import sys


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, diff: int) -> None:
        while index <= self.size:
            self.tree[index] += diff
            index += index & -index

    def query(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def interval_sum(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)


def solve(data: str) -> str:
    nums = [int(x) for x in data.split()]
    if not nums:
        return ""

    n = nums[0]
    q = nums[1]
    idx = 2

    bit = FenwickTree(n)
    status = [0] * (n + 1)
    output = []

    for _ in range(q):
        op = nums[idx]
        idx += 1

        if op == 1:
            i = nums[idx]
            idx += 1

            # 0: 增函數, 1: 減函數；每次操作都做切換。
            if status[i] == 0:
                status[i] = 1
                bit.update(i, 1)
            else:
                status[i] = 0
                bit.update(i, -1)
        else:
            left = nums[idx]
            right = nums[idx + 1]
            idx += 2

            down_count = bit.interval_sum(left, right)
            # 複合函數中減函數個數為奇數 -> 最後為減函數。
            output.append("1" if (down_count % 2 == 1) else "0")

    return "\n".join(output)


def main() -> None:
    input_data = sys.stdin.read()
    ans = solve(input_data)
    if ans:
        sys.stdout.write(ans)


if __name__ == "__main__":
    main()

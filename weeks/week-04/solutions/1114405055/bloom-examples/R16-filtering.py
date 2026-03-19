# R16. 過濾：推導式 / generator / filter / compress（1.16）

from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 1) list comprehension：立刻產生完整結果。
positives = [n for n in mylist if n > 0]
print("positives:", positives)

# 2) generator expression：延後計算，逐步取值。
positive_gen = (n for n in mylist if n > 0)
print("first two from generator:", next(positive_gen), next(positive_gen))

values = ["1", "2", "-3", "-", "N/A", "5"]


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


# 3) filter + 函式：把可轉成 int 的字串留下。
valid_int_text = list(filter(is_int, values))
print("valid int text:", valid_int_text)

addresses = ["a1", "a2", "a3", "a4"]
counts = [0, 3, 10, 7]
selectors = [count > 5 for count in counts]

# 4) compress：依布林遮罩篩選另一個序列。
print("count > 5:", list(compress(addresses, selectors)))

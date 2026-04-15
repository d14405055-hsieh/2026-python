# R12: Counter and most_common

from collections import Counter


words = ["look", "into", "my", "eyes", "look", "into", "my", "eyes", "eyes"]
word_counts = Counter(words)

print("top 3 ->", word_counts.most_common(3))

word_counts.update(["eyes", "eyes", "look"])
print("after update ->", word_counts)

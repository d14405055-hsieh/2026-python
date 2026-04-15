# R3: deque usage

from collections import deque


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print("fixed-size deque ->", q)

q.append(4)
print("after append(4) ->", q)

q2 = deque()
q2.append(1)
q2.appendleft(2)
print("append/appendleft ->", q2)

right = q2.pop()
left = q2.popleft()
print("pop values ->", right, left)

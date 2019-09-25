from collections import deque

# Deque Generalization of stacks and queues, append() & pop() from both sides
d = deque("elloo")
print(d)
d.appendleft('H')
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.rotate(1)
print(d)

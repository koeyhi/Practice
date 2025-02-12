from collections import deque

s = input()
queue = deque(s)
x = queue.popleft()
result = 10

while queue:
    y = queue.popleft()
    if y != x:
        result += 10
    else:
        result += 5
    x = y

print(result)
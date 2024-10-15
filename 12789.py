from collections import deque

n = int(input())
line = deque(map(int, input().split()))
stack = []
target = 1

while line:
    if line[0] == target:
        line.popleft()
        target += 1
    else:
        stack.append(line.popleft())

    while stack and stack[-1] == target:
        stack.pop()
        target += 1

if not stack:
    print("Nice")
else:
    print("Sad")

from collections import deque

n, k = map(int, input().split())
result = []

stack = deque(range(1, n + 1))
while stack:
    stack.rotate(-k)
    result.append(stack.pop())
print(f"<{', '.join(map(str, result))}>")

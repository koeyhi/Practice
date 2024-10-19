from collections import deque

n = int(input())
balloons = list(map(int, input().split()))

q = deque((i + 1, balloons[i]) for i in range(n))
result = []

while q:
    index, move = q.popleft()
    result.append(index)

    if not q:
        break

    if move > 0:
        q.rotate(-(move - 1))
    else:
        q.rotate(-move)

print(" ".join(map(str, result)))

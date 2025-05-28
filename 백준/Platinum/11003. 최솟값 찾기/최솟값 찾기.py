import sys
from collections import deque

input = sys.stdin.readline

n, L = map(int, input().split())
A = list(map(int, input().split()))

q = deque()
result = []

for i in range(n):
    while q and q[0][0] < i - L + 1:
        q.popleft()

    while q and q[-1][1] > A[i]:
        q.pop()

    q.append((i, A[i]))

    result.append(q[0][1])

print(*result)
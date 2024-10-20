from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

queue = deque()

for i in range(n):
    if a[i] == 0:
        queue.append(b[i])

result = []

for x in c:
    queue.appendleft(x)
    result.append(queue.pop())

print(" ".join(map(str, result)))

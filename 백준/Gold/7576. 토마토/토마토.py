from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append((nx, ny))

days = max(map(max, box)) - 1

for row in box:
    if 0 in row:
        days = -1
        break

print(days)
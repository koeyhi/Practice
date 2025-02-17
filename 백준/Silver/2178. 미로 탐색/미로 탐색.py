from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [[int(x) for x in str(input().strip())] for _ in range(n)]
queue = deque([(0, 0)])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maze[nx][ny] == 0:
            continue
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))

print(maze[n - 1][m - 1])
from collections import deque

n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if ground[i][j] == 0:
            dist[i][j] = 0
        if ground[i][j] == 2:
            dest_x, dest_y = i, j
            dist[i][j] = 0

queue = deque()
queue.append((dest_x, dest_y))
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] != -1:
            continue
        if ground[nx][ny] == 0:
            dist[nx][ny] = 0
        if ground[nx][ny] == 1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

for i in range(0, n):
    print(*dist[i])

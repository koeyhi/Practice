from collections import deque


def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = 1
    count = 1

    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = 1
                stack.append((nx, ny))
                count += 1

    return count


n = int(input())
graph = [[int(x) for x in input().strip()] for _ in range(n)]
visited = [[0] * n for _ in range(n)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            answer.append(dfs(i, j))

print(len(answer))
for ans in sorted(answer):
    print(ans)

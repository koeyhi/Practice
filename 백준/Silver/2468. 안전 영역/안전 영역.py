from collections import deque


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def count_safe(h):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and area[i][j] > h:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < n
                            and 0 <= ny < n
                            and not visited[nx][ny]
                            and area[nx][ny] > h
                        ):
                            visited[nx][ny] = True
                            q.append((nx, ny))

    return cnt


max_height = max(max(row) for row in area)
answer = 0

for water in range(max_height):
    answer = max(answer, count_safe(water))

print(answer)
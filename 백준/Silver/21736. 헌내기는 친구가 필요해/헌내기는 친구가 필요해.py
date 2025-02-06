from collections import deque

# 1. 입력 받기
n, m = map(int, input().split())
campus = [input() for _ in range(n)]

# 2. 시작 지점 찾기
for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            start = (i, j)
            break


def bfs(start):
    # 3. BFS 탐색 준비
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    people = 0

    # 4. BFS 탐색 진행
    while queue:
        x, y = queue.popleft()

        # 현재 칸이 P인 경우 사람 수 증가
        if campus[x][y] == "P":
            people += 1

        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 새로운 칸이 범위 내에 있고 방문하지 않았으며, 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니고 방문하지 않은 경우 큐에 추가
                if not visited[nx][ny] and campus[nx][ny] != "X":
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    if people == 0:
        print("TT")
    else:
        print(people)

bfs(start)
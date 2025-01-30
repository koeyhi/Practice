import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x, y + 1)
        return True
    return False


t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    ground = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        ground[x][y] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                dfs(ground, i, j)
                count += 1

    print(count)
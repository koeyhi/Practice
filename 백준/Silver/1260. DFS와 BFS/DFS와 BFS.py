from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    dfs_result.append(v)

    for adj in graph[v]:
        if not visited[adj]:
            dfs(graph, adj, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        bfs_result.append(current)

        for adj in graph[current]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    graph[i].sort()

dfs_result = []
bfs_result = []

visited_dfs = [False] * (N + 1)
dfs(graph, V, visited_dfs)

visited_bfs = [False] * (N + 1)
bfs(graph, V, visited_bfs)

print(*dfs_result)
print(*bfs_result)
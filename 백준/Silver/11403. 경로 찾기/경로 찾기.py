from collections import deque

# bfs
# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# result = [[0] * N for _ in range(N)]

# for start in range(N):
#     visited = [False] * N
#     queue = deque([start])
    
#     while queue:
#         current = queue.popleft()
        
#         for next_node in range(N):
#             if graph[current][next_node] == 1 and not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#                 result[start][next_node] = 1

# for row in result:
#     print(*row)

# 플로이드 워셜
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for row in graph:
    print(*row)
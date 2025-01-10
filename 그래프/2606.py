from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)  # 각 컴퓨터에 연결된 컴퓨터 번호를 리스트로 저장
    graph[v].append(u)

visited = [False] * (n + 1)
queue = deque([1])
visited[1] = True
count = 0

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            queue.append(neighbor)
            visited[neighbor] = True
            count += 1  # 새로 감염된 컴퓨터로 카운트

print(count)

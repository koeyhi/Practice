from collections import deque


def bfs(start):
    dist = [0] * (n + 1)
    visited = [False] * (n + 1)

    queue = deque([start])
    visited[start] = True
    dist[start] = 0

    while queue:
        current = queue.popleft()
        for nxt in friends[current]:
            if not visited[nxt]:
                visited[nxt] = True
                dist[nxt] = dist[current] + 1
                queue.append(nxt)

    return sum(dist)


n, m = map(int, input().split())
friends = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

distances = [(bfs(i), i) for i in range(1, n + 1)]
print(min(distances)[1])

# 플로이드-워셜 알고리즘 사용 가능
# 플로이드-워셜 사용 시 시간복잡도 O(N^3)이므로 N이 너무 크면 사용 불가능
from collections import deque

n, k = map(int, input().split())
dist = [-1] * 100001

queue = deque()

queue.append(n)
dist[n] = 0

while queue:
    x = queue.popleft()
    
    if x == k:
        print(dist[x])
        break
    
    for nx in [x - 1, x + 1, 2 * x]:
        if 0 <= nx < 100001 and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            queue.append(nx)
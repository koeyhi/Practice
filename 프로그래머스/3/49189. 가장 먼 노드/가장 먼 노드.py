from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    queue = deque([1])
    distance = [-1] * (n + 1)
    distance[1] = 0
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] < 0:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    
    return distance.count(max(distance))
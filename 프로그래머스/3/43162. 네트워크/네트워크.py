def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for connect in range(n):
            if computers[node][connect] == 1 and not visited[connect]:
                dfs(connect)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer
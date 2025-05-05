def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        
        for i in range(n):
            if computers[node][i] == 1 and visited[i] == False:
                dfs(i)
    
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1
    
    return answer
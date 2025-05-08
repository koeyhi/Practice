def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = -1
        
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if dp[y][x] == -1:
                continue
            if dp[y-1][x] > 0:
                dp[y][x] = (dp[y][x] + dp[y-1][x]) % 1_000_000_007
            if dp[y][x-1] > 0:
                dp[y][x] = (dp[y][x] + dp[y][x-1]) % 1_000_000_007
    return dp[n][m]
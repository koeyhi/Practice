def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        concat_num = int(str(N) * i)
        dp[i].add(concat_num)
        
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].update({a + b, a - b, a * b})
                    if b != 0:
                        dp[i].add(a // b)
        
        if number in dp[i]:
            return i
    
    return -1
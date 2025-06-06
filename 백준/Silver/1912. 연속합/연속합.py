n = int(input())
lst = list(map(int, input().split()))
dp = [0] * n
dp[0] = lst[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + lst[i], lst[i])

print(max(dp))
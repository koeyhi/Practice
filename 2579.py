n = int(input())
steps = [0]

for _ in range(n):
    steps.append(int(input()))

dp = [0] * (n + 1)
dp[1] = steps[1]

if n > 1:
    dp[2] = steps[1] + steps[2]

for i in range(3, n + 1):
    dp[i] = max(
        steps[i] + dp[i - 2],  # 2계단 전까지 최대값 + 현재 계단 값
        steps[i - 1]
        + steps[i]
        + dp[i - 3],  # 3계단 전까지 최대값 + 직전 계단 값 + 현재 계단 값
    )

print(dp[n])

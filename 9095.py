t = int(input())


def sum_123(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sum_123(n - 3) + sum_123(n - 2) + sum_123(n - 1)


for _ in range(t):
    n = int(input())
    print(sum_123(n))

# t = int(input())

# dp = [0] * 12
# dp[1], dp[2], dp[3] = 1, 2, 4

# for i in range(4, 12):
#     dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

# for _ in range(t):
#     print(dp[int(input())])

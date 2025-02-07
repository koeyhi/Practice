from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))

# DP
dp = [1] * n

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 이분 탐색
# lis = []

# for num in A:
#     idx = bisect_left(lis, num)
#     if idx == len(lis):
#         lis.append(num)
#     else:
#         lis[idx] = num

# print(len(lis))
# n = int(input())
# count = 0
# for i in range(1, n - 1):
#     for j in range(i+1, n):
#         for k in range(j+1, n+1):
#             count += 1
# print(count, 3, sep="\n") # 시간초과

n = int(input())
count = n * (n - 1) * (n - 2) // 6
print(count, 3, sep="\n")

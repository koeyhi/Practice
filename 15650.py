from itertools import combinations

n, m = map(int, input().split())
for p in combinations(range(1, n + 1), m):
    print(" ".join(map(str, p)))

# n, m = map(int, input().split())
# result = []

# def backtrack(start, depth):
#     if depth == m:
#         print(' '.join(map(str, result)))
#         return

#     for i in range(start, n + 1):
#         result.append(i)
#         backtrack(i + 1, depth + 1)
#         result.pop()

# backtrack(1, 0)

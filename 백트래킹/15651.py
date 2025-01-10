from itertools import product

n, m = map(int, input().split())
for p in product(range(1, n + 1), repeat=m):
    print(" ".join(map(str, p)))

    # n, m = map(int, input().split())
    # result = []

    # def backtrack(depth):
    #     if depth == m:
    #         print(' '.join(map(str, result)))
    #         return

    #     for i in range(1, n + 1):
    #         result.append(i)
    #         backtrack(depth + 1)
    #         result.pop()

    # backtrack(0)

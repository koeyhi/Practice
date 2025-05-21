n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

prev = cost[0]

for i in range(1, n):
    r, g, b = cost[i]
    prev = [
        min(prev[1], prev[2]) + r,
        min(prev[0], prev[2]) + g,
        min(prev[0], prev[1]) + b,
    ]

print(min(prev))
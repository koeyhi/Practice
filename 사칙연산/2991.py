a, b, c, d = map(int, input().split())
p, m, n = map(int, input().split())
result = []

for k in [p, m, n]:
    result.append(
        (1 if 1 <= k % (a + b) <= a else 0) + (1 if 1 <= k % (c + d) <= c else 0)
    )

for i in result:
    print(i)

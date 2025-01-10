a, b = map(int, input().split())
c, d = map(int, input().split())

x, y = ((a * d) + (b * c)), (b * d)
i, j = x, y
while j > 0:
    i, j = j, i % j

print(int(x / i), int(y / i))

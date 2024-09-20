n = int(input())

loc = [tuple(map(int, input().split())) for _ in range(n)]

loc.sort()

for x, y in loc:
    print(x, y)

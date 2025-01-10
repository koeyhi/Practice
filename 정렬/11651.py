# n = int(input())
# loc = []

# for _ in range(n):
#     x, y = map(int, input().split())
#     loc.append((y, x))

# loc.sort()

# for x, y in loc:
#     print(y, x)

n = int(input())
loc = [tuple(map(int, input().split())) for _ in range(n)]

loc.sort(key=lambda x: (x[1], x[0]))  # y먼저 정렬 후 y가 같을 경우 x정렬

for x, y in loc:
    print(x, y)

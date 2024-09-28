n = int(input())
scores = list(map(int, input().split()))
x, y = map(int, input().split())

count = sum(1 for score in scores if score >= y)

print(round((x / 100) * n), count)

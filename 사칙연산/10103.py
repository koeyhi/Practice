n = int(input())
p, q = 100, 100

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        q -= a
    elif a < b:
        p -= b

print(p, q, end="\n")

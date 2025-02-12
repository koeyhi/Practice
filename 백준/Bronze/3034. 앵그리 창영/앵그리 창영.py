n, w, h = map(int, input().split())
for _ in range(n):
    l = int(input())
    if l <= (w ** 2 + h ** 2) ** 0.5:
        print("DA")
    else:
        print("NE")
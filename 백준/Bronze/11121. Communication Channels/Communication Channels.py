t = int(input())
for _ in range(t):
    p, q = input().split()
    if p == q:
        print("OK")
    else:
        print("ERROR")
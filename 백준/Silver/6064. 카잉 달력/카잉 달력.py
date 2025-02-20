import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    for i in range(x, M * N + 1, M):
        if i % N == y % N:
            print(i)
            break
    else:
        print(-1)

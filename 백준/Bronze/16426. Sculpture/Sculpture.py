r, c = map(int, input().split())
sculpture = [list(map(int, input().split())) for _ in range(r)]
answer = [[0] * c for _ in range(r)]

for i in range(1, r - 1):
    for j in range(1, c - 1):
        if (
            sculpture[i - 1][j] > sculpture[i][j]
            and sculpture[i][j - 1] > sculpture[i][j]
            and sculpture[i + 1][j] > sculpture[i][j]
            and sculpture[i][j + 1] > sculpture[i][j]
        ):
            answer[i][j] = 1

for i in range(r):
    print(" ".join(map(str, answer[i])))
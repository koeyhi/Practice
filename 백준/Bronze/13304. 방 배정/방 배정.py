from math import ceil


N, K = map(int, input().split())
count = [[0] * 7 for _ in range(2)]

for _ in range(N):
    S, Y = map(int, input().split())
    count[S][Y] += 1

answer = 0

answer += ceil((count[0][1] + count[1][1] + count[0][2] + count[1][2]) / K)
answer += ceil((count[0][3] + count[0][4]) / K)
answer += ceil((count[1][3] + count[1][4]) / K)
answer += ceil((count[0][5] + count[0][6]) / K)
answer += ceil((count[1][5] + count[1][6]) / K)

print(answer)
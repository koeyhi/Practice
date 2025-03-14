N, K = map(int, input().split())
count = [[0] * 7 for _ in range(2)]

for _ in range(N):
    S, Y = map(int, input().split())
    count[S][Y] += 1

answer = 0

for s in range(2):
    for y in range(1, 7):
        cnt = count[s][y]
        answer += (cnt + K - 1) // K

print(answer)
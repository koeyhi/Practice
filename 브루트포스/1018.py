m, n = map(int, input().split())
board = [input() for _ in range(m)]
pattern1 = ["WBWBWBWB", "BWBWBWBW"] * 4
pattern2 = ["BWBWBWBW", "WBWBWBWB"] * 4
reprint = 64

for i in range(m - 7):
    for j in range(n - 7):
        count1 = 0
        count2 = 0
        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != pattern1[x][y]:
                    count1 += 1
                if board[i + x][j + y] != pattern2[x][y]:
                    count2 += 1
        reprint = min(reprint, count1, count2)

print(reprint)

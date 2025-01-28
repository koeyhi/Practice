n = int(input())
paper = []
white = 0
blue = 0

for i in range(n):
    l = list(map(int, input().split()))
    paper.append(l)

def paper_split(paper, n):
    global white, blue
    check = paper[0][0]
    for i in range(n):
        for j in range(n):
            if check != paper[i][j]:
                paper_split([row[:n//2] for row in paper[:n//2]], n//2)
                paper_split([row[n//2:] for row in paper[:n//2]], n//2)
                paper_split([row[:n//2] for row in paper[n//2:]], n//2)
                paper_split([row[n//2:] for row in paper[n//2:]], n//2)
                return
    if check == 0:
        white += 1
    else:
        blue += 1

paper_split(paper, n)
print(white)
print(blue)
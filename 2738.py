n, m = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    matrix2 = list(map(int, input().split()))
    result = [matrix1[i][j] + matrix2[j] for j in range(m)]
    print(' '.join(map(str, result)))
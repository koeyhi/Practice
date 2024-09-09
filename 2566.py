mat = [list(map(int, input().split())) for _ in range(9)]
max_num = max(max(row) for row in mat)
max_row, max_col = [(i, row.index(max_num)) for i, row in enumerate(mat) if max_num in row][0]
            
print(max_num)
print(max_row + 1, max_col + 1)
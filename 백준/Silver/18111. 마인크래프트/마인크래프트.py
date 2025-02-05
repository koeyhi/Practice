import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

min_height = min(map(min, ground))
max_height = max(map(max, ground))

best_time = float("inf")
best_height = 0

for h in range(min_height, max_height + 1):
    remove_block = 0
    add_block = 0
    
    for i in range(n):
        for j in range(m):
            if ground[i][j] < h:
                add_block += h - ground[i][j]
            else:
                remove_block += ground[i][j] - h
            
    if remove_block + b >= add_block:
        time = 2 * remove_block + add_block
        
        if time < best_time or (time == best_time and h > best_height):
            best_time = time
            best_height = h

print(best_time, best_height)
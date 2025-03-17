M = int(input())
direction = 0
rotation_num = 0

for _ in range(M):
    a, b, s = map(int, input().split())

    direction += s
    if rotation_num == 0:
        rotation_num = b / a
    else:
        rotation_num = (rotation_num / a) * b

direction = 1 if direction % 2 == 1 else 0
print(direction, int(rotation_num))
T = int(input())

for _ in range(T):
    cent = int(input())
    change = []
    for ch in [25, 10, 5, 1]:
        change.append(cent // ch)
        cent %= ch
    print(' '.join(map(str, change)))

# T = int(input())
# cent = []

# for i in range(T):
#     cent.append(int(input()))

# for x in cent:
#     change = []
#     change.append(x // 25)
#     x %= 25
#     change.append(x // 10)
#     x %= 10
#     change.append(x // 5)
#     x %= 5
#     change.append(x // 1)
#     print(' '.join(map(str, change)))
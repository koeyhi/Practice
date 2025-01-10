N, M = map(int, input().split())
S = input()
for _ in range(M):
    password = input()
    idx = 0
    can_make = False

    for p in password:
        if idx == len(S):
            break
        if p == S[idx]:
            idx += 1
            if idx == len(S):
                can_make = True
                break

    if can_make:
        print("true")
    else:
        print("false")

N = int(input())
mascot = input()
K = int(input())

if mascot == "annyong":
    if K % 2 == 1:
        print(K)
    elif K == 0:
        print(1)
    else:
        print(K - 1)
else:
    if K % 2 == 0:
        print(K)
    elif K == N:
        print(N - 1)
    else:
        print(K + 1)
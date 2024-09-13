T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        print(f"{H}{str(N//H).zfill(2)}")
    else:
        print(f"{N%H}{str((N//H)+1).zfill(2)}")  # zfill 활용

# T = int(input())

# for i in range(T):
#     H, W, N = map(int, input().split())

#     floor = H if N % H == 0 else N % H
#     room = (N // H) + 1

#     print(f"{floor}{str(room).zfill(2)}")

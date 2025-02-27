N = int(input())
for i in range(2 * N - 1):
    if i < N:
        print(" " * i + "*" * (N - i - 1) + "*" + "*" * (N - i - 1))
    else:
        print(" " * (2 * N - i - 2) + "*" * (i - N + 1) + "*" + "*" * (i - N + 1))
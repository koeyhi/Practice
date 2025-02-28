T = int(input())
for _ in range(T):
    M, C = input().split()
    chars = list(input().split())
    if C == "C":
        for char in chars:
            print(ord(char) - 64, end=" ")
        print()
    else:
        for char in chars:
            print(chr(int(char) + 64), end=" ")
        print()
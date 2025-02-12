n = int(input())

for _ in range(n):
    print("@@@" * n + " " * n + "@" * n)

for _ in range(n):
    print("@" * n + " " * n + "@" * n + " " * n + "@" * n)
    print("@" * n + " " * n + "@" * n + " " * n + "@" * n)
    print("@" * n + " " * n + "@" * n + " " * n + "@" * n)

for _ in range(n):
    print("@" * n + " " * n + "@@@" * n)
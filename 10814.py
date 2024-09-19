# n = int(input())
# users = []

# for i in range(n):
#     age, name = input().split()
#     users.append((age, name))

# users.sort(key=lambda x: int(x[0]))  # 튜플의 첫 요소만 이용해서 정렬

# for user in users:
#     print(" ".join(user))

import sys

n = int(sys.stdin.readline())
users = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    users.append((int(age), name))

users.sort(key=lambda x: x[0])  # 튜플의 첫 요소만 이용해서 정렬

for user in users:
    sys.stdout.write(f"{user[0]} {user[1]}\n")

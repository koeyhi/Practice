import sys

input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    action = input().split()
    if action[0] == "add":
        s.add(int(action[1]))
    elif action[0] == "remove":
        if int(action[1]) in s:
            s.remove(int(action[1]))
    elif action[0] == "check":
        print(1 if int(action[1]) in s else 0)
    elif action[0] == "toggle":
        if int(action[1]) in s:
            s.remove(int(action[1]))
        else:
            s.add(int(action[1]))
    elif action[0] == "all":
        s = set(range(1, 21))
    elif action[0] == "empty":
        s.clear()

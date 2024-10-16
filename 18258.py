import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
stack = deque()

for _ in range(n):
    comm = input().split()
    if comm[0] == "push":
        stack.append(comm[1])
    elif comm[0] == "pop":
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif comm[0] == "size":
        print(len(stack))
    elif comm[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif comm[0] == "front":
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif comm[0] == "back":
        if stack:
            print(stack[-1])
        else:
            print(-1)

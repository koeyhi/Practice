from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
stack = deque()

for _ in range(n):
    comm = list(map(int, input().split()))
    if comm[0] == 1:
        stack.appendleft(comm[1])
    elif comm[0] == 2:
        stack.append(comm[1])
    elif comm[0] == 3:
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif comm[0] == 4:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif comm[0] == 5:
        print(len(stack))
    elif comm[0] == 6:
        if stack:
            print(0)
        else:
            print(1)
    elif comm[0] == 7:
        if stack:
            print(stack[0])
        else:
            print(-1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)

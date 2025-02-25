from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    x = input().strip()[1:-1].split(",")
    if n == 0:
        x = deque()
    else:
        x = deque(map(int, x))
    reversed_p = False

    for command in p:
        if command == "R":
            reversed_p = not reversed_p

        elif command == "D":
            if not x:
                print("error")
                break
            else:
                if reversed_p:
                    x.pop()
                else:
                    x.popleft()
    else:
        if reversed_p:
            x.reverse()
        print("[" + ",".join(map(str, x)) + "]")

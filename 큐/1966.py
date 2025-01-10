from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    q = list(enumerate(map(int, input().split())))
    count = 0
    while True:
        if q[0][1] == max(q, key=lambda x: x[1])[1]:
            count += 1
            if q[0][0] == m:
                print(count)
                break
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))

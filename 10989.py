import sys

count = [0] * 10001
n = int(input())

for _ in range(n):
    m = int(sys.stdin.readline())
    count[m] += 1

for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)

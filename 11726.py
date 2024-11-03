import sys

input = sys.stdin.readline

n = int(input())
rectangles = [0] * (n + 1)

rectangles[1] = 1

if n > 1:
    rectangles[2] = 2

for i in range(3, n + 1):
    rectangles[i] = (rectangles[i - 1] + rectangles[i - 2]) % 10007

print(rectangles[n])

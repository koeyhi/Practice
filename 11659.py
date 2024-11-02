import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

sum_numbers = [0] * (n + 1)
sum_numbers[1] = numbers[0]

for i in range(2, n + 1):
    sum_numbers[i] = numbers[i - 1] + sum_numbers[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(sum_numbers[j] - sum_numbers[i - 1])

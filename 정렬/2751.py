import sys

n = int(sys.stdin.readline())  # 빠른 입력이 필요할 때 사용
numbers = [int(sys.stdin.readline()) for _ in range(n)]

numbers.sort()

for i in numbers:
    print(i)

n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

numbers.sort()

for i in numbers:
    print(i)

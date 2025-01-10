import math

n = int(input())
f = math.factorial(n)
length = len(str(f))
count = 0

for i in range(-1, -length, -1):
    if str(f)[i] == "0":
        count += 1
    else:
        break

print(count)

# n = int(input()) # 5의 개수만큼 0 발생, 25, 125 등은 2개, 3개씩 0이 발생함

# count = 0
# i = 5
# while n // i > 0:
#     count += n // i
#     i *= 5

# print(count)

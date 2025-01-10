X = int(input())
n, i = 0, 1

while True:
    n += i
    if X <= n:
        break
    i += 1

position = X - (n - i)

if i % 2 == 0:
    a, b = position, i - position + 1
else:
    a, b = i - position + 1, position

print(f"{a}/{b}")

# X = int(input())
# n, i = 0, 1

# while True:
#     n += i
#     if X <= n:
#         break
#     i += 1

# if i % 2 == 0:
#     a, b = 1, i
#     for k in range(1, X - (n - i)):
#         a += 1
#         b -= 1
# else:
#     a, b = i, 1
#     for k in range(1, X - (n - i)):
#         a -= 1
#         b += 1

# print(f"{a}/{b}")

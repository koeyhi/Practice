n = int(input())
x = n // 5

while x >= 0:
    if (n - (5 * x)) % 3 == 0:
        y = (n - (5 * x)) // 3
        print(x + y)
        break
    x -= 1
else:
    print(-1)

# n = int(input())
# x = n // 5

# while x >= 0:
#     if x == 0:
#         if n % 3 != 0:
#             print(-1)

#     if (n - (5 * x)) % 3 == 0:
#         print(x + (n - (5 * x)) // 3)
#         break
#     else:
#         x -= 1

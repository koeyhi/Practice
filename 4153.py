while True:
    sides = list(map(int, input().split()))
    if sides[0] == 0:
        break
    sides.sort()
    if sides[2] ** 2 == (sides[0] ** 2) + (sides[1] ** 2):
        print("right")
    else:
        print("wrong")

# while True:
#     a, b, c = map(int, input().split())

#     if a == 0:
#         break

#     if a > b and a > c:
#         if a**2 == (b**2) + (c**2):
#             print("right")
#         else:
#             print("wrong")
#     if b > a and b > c:
#         if b**2 == (a**2) + (c**2):
#             print("right")
#         else:
#             print("wrong")
#     if c > a and c > b:
#         if c**2 == (a**2) + (b**2):
#             print("right")
#         else:
#             print("wrong")

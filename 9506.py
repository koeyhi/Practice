# while True:
#     n = int(input())
#     if n == -1:
#         break
#     lst = [i for i in range(1, (n // 2) + 1) if n % i == 0]
#     output = f"{n} = "
#     if sum(lst) == n:
#         for num in lst:
#             output += str(num)
#             if num != lst[-1]:
#                 output += " + "
#         print(output)
#     else:
#         print(f"{n} is NOT perfect.")

while True:
    n = int(input())
    if n == -1:
        break

    divisors = [i for i in range(1, (n // 2) + 1) if n % i == 0]

    if sum(divisors) == n:
        divisors_str = " + ".join(str(c) for c in divisors)
        print(f"{n} = {divisors_str}")
    else:
        print(f"{n} is NOT perfect.")

import math


def gcd_multiple_numbers(numbers):
    gcd_result = numbers[0]
    for num in numbers[1:]:
        gcd_result = math.gcd(gcd_result, num)
    return gcd_result


def solve():
    n = int(input())
    positions = [int(input()) for _ in range(n)]

    gaps = [positions[i + 1] - positions[i] for i in range(n - 1)]

    gcd_value = gcd_multiple_numbers(gaps)

    additional_trees = 0
    for gap in gaps:
        additional_trees += (gap // gcd_value) - 1

    print(additional_trees)


solve()

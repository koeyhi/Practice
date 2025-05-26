from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    candidates = set()
    nums = list(numbers)
    for k in range(1, len(nums) + 1):
        for perm in permutations(nums, k):
            num = int("".join(perm))
            candidates.add(num)

    count = 0
    for num in candidates:
        if is_prime(num):
            count += 1

    return count
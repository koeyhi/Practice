import math

def to_base_k(n, k):
    if n < k:
        return str(n)
    return to_base_k(n // k, k) + str(n % k)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    l = int(math.isqrt(n))
    i = 5
    while i <= l:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
def solution(n, k):
    trans = to_base_k(n, k)
    return sum(is_prime(int(t)) for t in trans.split('0') if t)
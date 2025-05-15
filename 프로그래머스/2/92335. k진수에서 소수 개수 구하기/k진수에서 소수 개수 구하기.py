def to_base_k(n, k):
    if n < k:
        return str(n)
    return to_base_k(n // k, k) + str(n % k)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    trans = to_base_k(n, k)
    return sum(is_prime(int(t)) for t in trans.split('0') if t)
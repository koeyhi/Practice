import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = numer1 * denom2 + numer2 * denom1
    b = denom1 * denom2
    g = math.gcd(a, b)
    
    answer.append(a // g)
    answer.append(b // g)
    
    return answer
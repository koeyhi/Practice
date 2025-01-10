n, m = map(int, input().split())


def gcd(a, b):  # 최대공약수
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):  # 최소공배수
    return (a * b) // gcd(a, b)


print(gcd(n, m), lcm(n, m), sep="\n")

# math 라이브러리 사용
# import math

# a, b = map(int, input().split())
# print(math.gcd(a, b), math.lcm(a, b), sep="\n")

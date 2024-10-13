def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)  # 모든 수가 소수라고 가정
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아니므로 False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:  # i 가 소수일 경우
            for j in range(i * i, limit + 1, i):  # i**2 부터 i 의 배수를 False로 설정
                is_prime[j] = False
    return is_prime


limit = 123456 * 2
prime_list = sieve_of_eratosthenes(limit)

while True:
    n = int(input())
    if n == 0:
        break

    count = sum(prime_list[n + 1 : 2 * n + 1])

    print(count)

is_prime = [True] * (1000001)
is_prime[0] = is_prime[1] = False

for i in range(2, 500001):
    if is_prime[i]:
        for j in range(i * i, 1000001, i):
            is_prime[j] = False


T = int(input())

for i in range(T):
    n = int(input())
    count = 0

    for j in range(1, int(n * 0.5) + 1):
        if is_prime[j] and is_prime[n - j]:
            count += 1
    print(count)

t = int(input())

for _ in range(t):
    count = 0
    a, b, c = map(int, input().split())
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                if i % j == j % k and j % k == k % i:
                    count += 1

    print(count)

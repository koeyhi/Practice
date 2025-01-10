N = int(input())
start = max(1, N - (9 * len(str(N))))  # N 이 한 자리 수일 때는 1

for i in range(start, N):
    generator_sum = i + sum(map(int, str(i)))
    if generator_sum == N:
        print(i)
        break
else:
    print(0)

n = int(input())
time = list(map(int, input().split()))

order = sorted(time)
total_time = 0

for p in order:
    total_time += p * n
    n -= 1

print(total_time)

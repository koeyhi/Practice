now = input()
N = int(input())
count = 0

for _ in range(N):
    fire_date = input()
    if fire_date >= now:
        count += 1

print(count)
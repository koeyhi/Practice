N = int(input())
time = []
meeting = 0

for _ in range(N):
    time.append(tuple(map(int, input().split())))

time.sort(key=lambda x: (x[1], x[0]))
end = 0

for s, e in time:
    if s >= end:
        end = e
        meeting += 1

print(meeting)
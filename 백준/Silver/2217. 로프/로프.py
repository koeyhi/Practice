N = int(input())
ropes = []
count = 1

for _ in range(N):
    w = int(input())
    ropes.append(w)

ropes.sort(reverse=True)
max_weight = []

for rope in ropes:
    weight = rope * count
    max_weight.append(weight)
    count += 1

print(max(max_weight))
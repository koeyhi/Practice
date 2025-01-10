x, y = [], []

for _ in range(3):
    a, b = map(int, input().split())
    x.append(a), y.append(b)

print([i for i in x if x.count(i) == 1][0], [i for i in y if y.count(i) == 1][0])

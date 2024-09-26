n = int(input())
m = int(input())

result = []

for i in range(n, m + 1):
    balanced = True
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            balanced = False
            break
    if balanced:
        result.append(i)

if result:
    print(sum(result), min(result), sep="\n")
else:
    print(-1)

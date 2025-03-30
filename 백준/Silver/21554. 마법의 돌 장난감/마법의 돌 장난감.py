N = int(input())
toy_size = list(map(int, input().split()))
operation = []

for i in range(N):
    correct = i + 1

    if toy_size[i] != correct:
        j = toy_size.index(correct)
        toy_size[i : j + 1] = toy_size[i : j + 1][::-1]
        operation.append((i + 1, j + 1))

if len(operation) > 100:
    print(-1)
else:
    print(len(operation))
    for i in operation:
        print(i[0], i[1])
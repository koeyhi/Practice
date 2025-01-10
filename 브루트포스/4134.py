n = int(input())

for _ in range(n):
    i = int(input())
    k = 0

    while True:
        prime = True
        if i + k < 2:
            prime = False

        for t in range(2, int((i + k) ** 0.5) + 1):
            if (i + k) % t == 0:
                prime = False
                break

        if prime is True:
            print(i + k)
            break
        else:
            k += 1

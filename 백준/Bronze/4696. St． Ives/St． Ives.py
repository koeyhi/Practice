while True:
    w = float(input())
    if w == 0:
        break
    print(f"{1 + w + (w ** 2) + (w ** 3) + (w ** 4):.2f}")
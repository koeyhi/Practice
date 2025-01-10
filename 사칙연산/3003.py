pieces = input().split()
needs = [1, 1, 2, 2, 2, 8]
lst = [ n - int(p) for p, n in zip(pieces, needs)]
print(*lst)
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

tshirts = sum((size // T) + 1 if size % T != 0 else size // T for size in sizes)
bundle, each = N // P, N % P

print(tshirts)
print(bundle, each)

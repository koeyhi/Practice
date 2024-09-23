n, k = map(int, input().split())

lst = [i for i in range(1, (n // 2) + 1) if n % i == 0]
lst.append(n)

if k > len(lst):
    print(0)
else:
    print(lst[k - 1])

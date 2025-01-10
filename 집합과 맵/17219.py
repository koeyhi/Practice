n, m = map(int, input().split())
memo = {}

for _ in range(n):
    data = input().split()
    memo[data[0]] = data[1]

for _ in range(m):
    print(memo[input()])

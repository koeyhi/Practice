n, k = map(int, input().split())
coin_list = []
result = 0

for _ in range(n):
    coin_list.append(int(input()))

i = len(coin_list) - 1
while k > 0:
    result += k // coin_list[i]
    k %= coin_list[i]
    i -= 1

print(result)

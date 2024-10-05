import sys

input = sys.stdin.readline

n, m = map(int, input().split())
poke_list = []
poke_dict = {}

for i in range(n):
    poke_list.append(input().strip())
    poke_dict[poke_list[i]] = i + 1

for i in range(m):
    t = input().strip()
    if t.isdigit():
        print(poke_list[int(t) - 1])
    else:
        print(poke_dict[t])

import sys

n = int(sys.stdin.readline())
sangeun_have = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
which_have = list(map(int, sys.stdin.readline().split()))

card_count = {}

for i in sangeun_have:
    if i in card_count.keys():
        card_count[i] += 1
    else:
        card_count[i] = 1

for i in which_have:
    print(card_count.get(i, 0), end=" ")

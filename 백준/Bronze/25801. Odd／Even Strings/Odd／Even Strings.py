from collections import Counter

S = input()
count = Counter(S)

all_even = all(v % 2 == 0 for v in count.values())
all_odd = all(v % 2 == 1 for v in count.values())

if all_even:
    print("0")
elif all_odd:
    print("1")
else:
    print("0/1")
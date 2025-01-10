from collections import Counter

n = int(input())

for _ in range(n):
    v = int(input())
    v_list = [int(input()) for _ in range(v)]

    counter = Counter(v_list)

    result = min([i for i in counter if counter[i] == max(counter.values())])

    print(result)

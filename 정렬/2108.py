import sys

input = sys.stdin.readline
n = int(input())
num_list = [int(input()) for _ in range(n)]
result = []

mean = round(sum(num_list) / n)

median = sorted(num_list)[n // 2]

count = {}
max_count = 0
for num in num_list:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1

    if count[num] > max_count:
        max_count = count[num]

mode_list = [i for i, v in count.items() if max_count == v]

if len(mode_list) > 1:
    mode = sorted(mode_list)[1]
else:
    mode = mode_list[0]

ran = max(num_list) - min(num_list)

print(mean, median, mode, ran, sep="\n")

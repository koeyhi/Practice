import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

count = 0
prefix = 0
freq = defaultdict(int)
freq[0] = 1

for x in A:
    prefix += x
    count += freq[prefix - k]
    freq[prefix] += 1

print(count)
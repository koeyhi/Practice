from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i in sorted(permutations(nums, m)):
    print(' '.join(map(str, i)))
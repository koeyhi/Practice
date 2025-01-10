n = int(input())
arr = list(map(int, input().split()))

sorted_unique = sorted(set(arr))

rank = {value: idx for idx, value in enumerate(sorted_unique)}

compressed = [rank[value] for value in arr]
print(" ".join(map(str, compressed)))

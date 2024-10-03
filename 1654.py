# 이진탐색
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

low, high = 1, max(lines)
result = 0

while low <= high:
    mid = (low + high) // 2
    total = sum([line // mid for line in lines])

    if total >= n:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)

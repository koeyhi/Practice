nums = list(map(int, input().split()))
result = sum([num**2 for num in nums])
print(result % 10)
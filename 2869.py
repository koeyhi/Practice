A, B, V = map(int, input().split())
total_distance = V - A
day_distance = A - B
days = 1 + len(range(0, total_distance, day_distance))
print(days)

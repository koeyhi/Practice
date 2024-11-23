n = int(input())
ids = set()
count = 0

for _ in range(n):
    id = input()
    if id != "ENTER":
        ids.add(id)
    else:
        count += len(ids)
        ids = set()

count += len(ids)
print(count)

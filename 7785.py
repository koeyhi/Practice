n = int(input())
employers = set()

for _ in range(n):
    record = input().split()
    if record[1] == "enter":
        employers.add(record[0])
    elif record[1] == "leave":
        employers.remove(record[0])

employers = list(employers)
print(*sorted(employers, reverse=True), sep="\n")

n, m = map(int, input().split())
no_heard = set()
no_saw = set()

for _ in range(n):
    no_heard.add(input())

for _ in range(m):
    no_saw.add(input())

result = list(no_heard.intersection(no_saw))
print(len(result))
for name in sorted(result):
    print(name)

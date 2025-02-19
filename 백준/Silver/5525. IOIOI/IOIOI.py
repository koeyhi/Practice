n = int(input())
m = int(input())
s = input()

pn = "IO" * n + "I"
count = 0

for i in range(m - 2 * n):
    if s[i:i + 2 * n + 1] == pn:
        count += 1

print(count)
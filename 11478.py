S = input()
strings = []

for i in range(1, len(S) + 1):
    for j in range(0, len(S) - i + 1):
        strings.append(S[j : j + i])

strings = set(strings)
print(len(strings))

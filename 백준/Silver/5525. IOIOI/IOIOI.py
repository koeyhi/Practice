n = int(input())
m = int(input())
s = input()

pattern_length = 0
count = 0
i = 0

while i < m - 1:
    if s[i:i + 3] == "IOI":
        pattern_length += 1
        if pattern_length >= n:
            count += 1
        i += 2
    else:
        pattern_length = 0
        i += 1

print(count)
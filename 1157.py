w = input().upper()
max_count = 0

for char in set(w):
    count = w.count(char)
    if count > max_count:
        max_count = count
        max_char = char
    elif count == max_count:
        max_char = "?"

print(max_char)
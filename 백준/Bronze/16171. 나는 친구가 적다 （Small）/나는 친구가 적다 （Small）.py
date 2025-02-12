s = input()
s_clear = ""
k = input()

for c in s:
    if c.isalpha():
        s_clear += c

if k in s_clear:
    print(1)
else:
    print(0)
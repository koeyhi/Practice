d, h, m = map(int, input().split())
time = 0

if m < 11:
    h -= 1
    m += 60
if h < 11:
    d -= 1
    h += 24
if d < 11:
    print(-1)
else:
    print((d - 11) * 24 * 60 + (h - 11) * 60 + (m - 11))
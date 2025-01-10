a, b, c, d, e, f = map(int, input().split())

# 분모 계산 (a * e - b * d)
denom = a * e - b * d

# 크래머의 법칙을 사용하여 x와 y 계산
x = (c * e - b * f) / denom
y = (a * f - c * d) / denom

# 결과 출력
print(int(x), int(y))

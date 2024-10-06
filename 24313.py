a1, a2 = map(int, input().split())
c = int(input())
n0 = int(input())

# f = a1 * n0 + a2
# g = c * n0
# f <= g
# a1 * n0 + a2 <= c * n0 # 양 변 정리
# n0 * (a1 - c) <= -a2 # a1 <= c

if a1 <= c and a1 * n0 + a2 <= c * n0:
    print(1)
else:
    print(0)

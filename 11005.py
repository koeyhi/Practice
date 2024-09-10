N, B = map(int, input().split())
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []

if N == 0:
        result.append(0)

while N:
        result.append(digits[N % B]) # 10진수를 B진법 수로 변환
        N //= B
        
print(''.join(result[::-1]))

# N, B = map(int, input().split())
# result = ''
# digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# while N:
#     result = digits[N % B] + result
#     N //= B
# print(result or '0')
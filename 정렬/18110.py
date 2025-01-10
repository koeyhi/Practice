n = int(input())

if n == 0:
    print(0)
else:
    d = [int(input()) for _ in range(n)]
    d.sort()

    exc = int((n * 0.15) + 0.5)

    if exc > 0:
        result = int((sum(d[exc:-exc]) / len(d[exc:-exc])) + 0.5)
    else:
        result = int((sum(d) / len(d)) + 0.5)

    print(result)

# 파이썬의 round 는 사사오입이 아닌 오사오입으로 처리함
# 5 미만의 숫자는 내림, 5 초과의 숫자는 올림
# 만약 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내림
# 따라서 반올림할 수에 0.5를 더해준 뒤 int 형식으로 변환하는 방식으로 반올림을 수행함

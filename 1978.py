N = int(input())
nums = map(int, input().split())
result = 0

for num in nums:
    if num == 1:
        continue
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        result += 1  # for, while 반복문이 정상적으로 완료되었을 때(break로 중간에 종료되지 않았을 때) else 블록 실행

print(result)

# for i in range(2, 10): # for else 예시
#     if i % 2 == 0:
#         print(f"{i}는 짝수입니다.")
#         break
# else:
#     print("모든 숫자는 홀수입니다.")

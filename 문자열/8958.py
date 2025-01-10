T = int(input())

for i in range(T):
    count = 0
    for c in input().split("X"):
        length = len(c)
        if length > 1:
            count += length * (length + 1) // 2
        elif length == 1:
            count += 1
    print(count)

# T = int(input())  # 테스트 케이스의 수 입력

# for _ in range(T):
#     result = input()  # OX 퀴즈 결과 문자열 입력
#     score = 0
#     current_score = 0

#     for char in result:
#         if char == 'O':
#             current_score += 1  # O가 연속되면 점수를 누적
#             score += current_score  # 총 점수에 추가
#         else:
#             current_score = 0  # X가 나오면 연속 점수 리셋

#     print(score)

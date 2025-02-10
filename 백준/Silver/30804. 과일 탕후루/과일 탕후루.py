# 부분 배열 중 가장 길이가 긴 구간 찾기
# 투 포인터 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

l, maxlength, distinct_count = 0, 0, 0
count = [0] * 10

for r in range(n):
    fruit = s[r]
    if count[fruit] == 0:
        distinct_count += 1
    count[fruit] += 1

    while distinct_count > 2:
        left_fruit = s[l]
        count[left_fruit] -= 1
        if count[left_fruit] == 0:
            distinct_count -= 1
        l += 1
    
    current_length = r - l + 1
    if current_length > maxlength:
        maxlength = current_length

print(maxlength)
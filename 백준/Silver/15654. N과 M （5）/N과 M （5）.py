# from itertools import permutations

# n, m = map(int, input().split())
# nums = list(map(int, input().split()))

# for i in sorted(permutations(nums, m)):
#     print(' '.join(map(str, i)))

def backtrack(depth):
    if depth == M:
        print(*result)
        return
    
    for i in range(N):
        if not visited[i]:  # 방문하지 않은 경우만 선택
            visited[i] = True
            result.append(nums[i])
            backtrack(depth + 1)
            result.pop()  # 원상복구 (백트래킹)
            visited[i] = False

# 입력 처리
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  # 오름차순 정렬

# 백트래킹을 위한 초기 설정
visited = [False] * N
result = []

backtrack(0)  # 백트래킹 시작

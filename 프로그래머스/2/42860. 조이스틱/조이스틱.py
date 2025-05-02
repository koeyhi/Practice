# def solution(name):
#     answer = 0
    
#     for c in name:
#         if c != 'A':
#             break
#         return 0
    
#     diff = [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name]
        
#     for i, char in enumerate(name[1:]):
#         if char != 'A':
#             right = i
#             break
    
#     for i, char in enumerate(name[-1:]):
#         if char != 'A':
#             left = i
#             break
    
#     if left <= right:
#         answer = sum(diff) + len(name) - right - 1
#     else:
#         answer = sum(diff) + len(name) - left - 1
    
#     return answer


def solution(name):
    n = len(name)
    diff = sum([min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name])  # 조이스틱 위아래 방향 총 횟수
    
    moves = n - 1
    for i in range(n):  # 조이스틱 좌우 방향 횟수
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':  # i 기준 뒤쪽 연속된 'A' 개수
            next_idx += 1
        
        moves = min(
            moves,  # 오른쪽 끝까지 이동
            2 * i + n - next_idx,  # 오른쪽 i번 이동, 왼쪽으로 쭉 돌아가기 (i + n - next_idx)
            i + 2 * (n - next_idx)  # 왼쪽 (n-next_idx)번 이동, 오른쪽으로 쭉 돌아오기 ((n - next_idx) + i)
        )
        
    return diff + moves
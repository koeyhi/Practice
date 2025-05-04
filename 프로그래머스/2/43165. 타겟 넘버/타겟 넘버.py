def solution(numbers, target):
    answer = 0
    
    def dfs(idx, current_sum):
        if idx == len(numbers):  # 모든 숫자를 다 사용했을 때
            return 1 if current_sum == target else 0  # 합이 타겟과 같으면 1 아니면 0
        
        # 현재 숫자를 더하는 경우와 빼는 경우 모두 탐색 및 더해서 반환
        return (
            dfs(idx + 1, current_sum + numbers[idx]) +
            dfs(idx + 1, current_sum - numbers[idx])
        )
    
    return dfs(0, 0)

# DFS 로 풀이 (재귀 호출)
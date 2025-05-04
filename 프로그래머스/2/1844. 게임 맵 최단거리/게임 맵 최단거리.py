from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 행, 열 개수
    queue = deque([(0, 0, 1)])  # 시작 위치, 이동 거리
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 상하좌우 방향 이동거리
    
    while queue:  # 큐가 빌 때까지
        x, y, dist = queue.popleft()  # 가장 먼저 들어온 위치의 거리 정보
        
        if x == n - 1 and y == m - 1:  # 도착 지점에 도달한 경우 이동거리 반환
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 각 방향으로 이동했을 때 위치
            
            # 맵 안쪽이면서 진행할 수 있는 위치이거나 이미 방문한 위치가 아닐 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny, dist + 1))  # 큐에 추가
                maps[nx][ny] = 0  # 방문한 위치는 0으로 채워 다시 방문하지 않도록 함
        
    return -1
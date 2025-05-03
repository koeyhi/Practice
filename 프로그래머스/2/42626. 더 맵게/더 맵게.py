import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        new = a + 2 * b
        heapq.heappush(scoville, new)
        answer += 1
        
        if len(scoville) == 1:
            break
    
    if scoville and scoville[0] < K:
        return -1
    
    return answer
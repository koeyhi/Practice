import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    
    heap = []
    time, total_wait = 0, 0
    idx, n = 0, len(jobs)
    
    while idx < n or heap:
        while idx < n and jobs[idx][0] <= time:
            req, dur = jobs[idx]
            heapq.heappush(heap, (dur, req))
            idx += 1
        
        if heap:
            dur, req = heapq.heappop(heap)
            time += dur
            total_wait += (time - req)
        else:
            time = jobs[idx][0]

    return total_wait // n
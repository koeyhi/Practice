import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = dict()
    uid = 0

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(min_heap, (num, uid))
            heapq.heappush(max_heap, (-num, uid))
            visited[uid] = True
            uid += 1

        else:
            if num == 1:
                while max_heap and not visited.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)
                if max_heap:
                    _, rid = heapq.heappop(max_heap)
                    visited[rid] = False

            else:  # num == -1
                while min_heap and not visited.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)
                if min_heap:
                    _, rid = heapq.heappop(min_heap)
                    visited[rid] = False

    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)
    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    if not min_heap:
        return [0, 0]
    max_val = -max_heap[0][0]
    min_val = min_heap[0][0]
    return [max_val, min_val]
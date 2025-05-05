from collections import deque

def solution(begin, target, words):
    visited = {begin}
    queue = deque([(begin, 0)])
    
    if target not in words:
        return 0
    
    def is_one_diff(a, b):
        diff_count = sum(1 for x, y in zip(a, b) if x != y)
        return diff_count == 1
    
    while queue:
        word, depth = queue.popleft()
        
        if word == target:
            return depth
        
        for w in words:
            if is_one_diff(word, w) and w not in visited:
                visited.add(w)
                queue.append((w, depth+1))
                
    return 0
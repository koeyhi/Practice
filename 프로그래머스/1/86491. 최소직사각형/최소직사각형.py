def solution(sizes):
    max_short = 0
    max_long = 0
    
    for w, h in sizes:
        short, long = min(w, h), max(w, h)
        
        if short > max_short:
            max_short = short
        if long > max_long:
            max_long = long
            
    return max_short * max_long
def solution(mats, park):
    mats.sort(reverse=True)
    park_height = len(park)
    park_width = len(park[0])
    
    for l in mats:
        for i in range(park_height - l + 1):
            for j in range(park_width - l + 1):
                is_placeable = True
                
                for a in range(l):
                    for b in range(l):
                        if park[i+a][j+b] != "-1":
                            is_placeable = False
                            break
                            
                    if not is_placeable:
                        break
                
                if is_placeable:
                    return l
    
    return -1
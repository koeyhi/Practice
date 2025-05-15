def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    m = len(timelogs[0])
    max_time = []
    weekday = [0 if ((d + startday) % 7 in (0, 6)) else 1 for d in range(m)]
    
    for i in range(n):
        if (schedules[i] + 10) % 100 >= 60:
            max_time.append(schedules[i] + 50)
        else:
            max_time.append(schedules[i] + 10)
    
    for i in range(n):
        event = [0] * m
        for j in range(m):
            if ((j + startday) % 7 not in (0, 6)) and timelogs[i][j] <= max_time[i]:
                event[j] = 1
        
        if event == weekday:
            answer += 1
    
    return answer
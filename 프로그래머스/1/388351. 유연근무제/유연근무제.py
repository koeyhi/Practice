def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    max_time = []
    weekday = [0 if ((d + startday) % 7 in (0, 6)) else 1 for d in range(7)]
    
    for i in range(n):
        if (schedules[i] + 10) % 100 >= 60:
            max_time.append(schedules[i] + 50)
        else:
            max_time.append(schedules[i] + 10)
    
    for i in range(n):
        event = [0] * 7
        for j in range(7):
            if ((j + startday) % 7 not in (0, 6)) and timelogs[i][j] <= max_time[i]:
                event[j] = 1
        
        if event == weekday:
            answer += 1
    
    return answer
N = int(input())
cost = 0
for _ in range(N):
    time, call_time = input().split()
    hour, minute = map(int, time.split(":"))
    call_time = int(call_time)

    if hour < 7 or hour >= 19:
        if hour == 6:
            if minute + call_time > 60:
                cost += (60 - minute) * 5 + (call_time - (60 - minute)) * 10
            else:
                cost += call_time * 5
        else:
            cost += call_time * 5
    else:
        if hour == 18:
            if minute + call_time > 60:
                cost += (60 - minute) * 10 + (call_time - (60 - minute)) * 5
            else:
                cost += call_time * 10
        else:
            cost += call_time * 10

print(cost)
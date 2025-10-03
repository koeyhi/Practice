def trans_time(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute
    
def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = trans_time(video_len), trans_time(pos), trans_time(op_start), trans_time(op_end)
    if op_start <= pos <= op_end:
        pos = op_end

    for i in range(len(commands)):
        if commands[i] == "next":
            pos += 10
        else:
            pos -= 10
        
        if pos < 0:
            pos = 0
        
        if pos > video_len:
            pos = video_len
        
        if op_start <= pos <= op_end:
            pos = op_end
    
    hour = pos // 60
    minute = pos % 60
    result = f"{hour:02d}:{minute:02d}"
    return result
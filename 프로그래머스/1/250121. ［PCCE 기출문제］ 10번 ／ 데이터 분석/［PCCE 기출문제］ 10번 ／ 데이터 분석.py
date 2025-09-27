# def solution(data, ext, val_ext, sort_by):
#     col = 0
#     content_condition = []
    
#     if ext == "code":
#         col = 0
#     elif ext == "date":
#         col = 1
#     elif ext == "maximum":
#         col = 2
#     else:
#         col = 3
    
#     for i in range(len(data)):
#         if data[i][col] < val_ext:
#             content_condition.append(data[i])
    
#     if sort_by == "code":
#         content_condition.sort(key=lambda x: x[0])
#     elif sort_by == "date":
#         content_condition.sort(key=lambda x: x[1])
#     elif sort_by == "maximum":
#         content_condition.sort(key=lambda x: x[2])
#     else:
#         content_condition.sort(key=lambda x: x[3])
    
#     return content_condition

def solution(data, ext, val_ext, sort_by):
    col_map = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    filtered_data = [d for d in data if d[col_map[ext]] < val_ext]
    
    answer = sorted(filtered_data, key=lambda x: x[col_map[sort_by]])
    
    return answer
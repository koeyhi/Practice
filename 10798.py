result = ''
str_list = [input() for _ in range(5)]

for i in range(len(max(str_list, key=len))):
    for j in range(5):
        try:
            result += str_list[j][i]
        except IndexError:
            continue
            
print(result)
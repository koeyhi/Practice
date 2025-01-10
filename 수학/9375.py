t = int(input())

for _ in range(t):
    clothes = {}
    n = int(input())
    for _ in range(n):
        clothes_name, clothes_type = input().split()
        if clothes_type in clothes:
            clothes[clothes_type].append(clothes_name)
        else:
            clothes[clothes_type] = [clothes_name]

    result = 1
    for clothes_list in clothes.values():
        result *= len(clothes_list) + 1  # 각 옷을 입는 경우 + 입지 않는 경우

    result -= 1  # 아예 안입는 경우 제외
    print(result)

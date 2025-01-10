num_list = [int(input()) for i in range(9)]

for i in range(len(num_list) - 1):
    for j in range(i + 1, len(num_list)):
        if sum(num_list) - num_list[i] - num_list[j] == 100:
            not_real = [num_list[i], num_list[j]]
            break

num_list.remove(not_real[0])
num_list.remove(not_real[1])

for i in num_list:
    print(i)

n, i = map(int, input().split())
handle_list = [input() for _ in range(n)]
print((sorted(handle_list)[i - 1]))

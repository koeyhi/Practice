n, m = map(int, input().split())
n_set = set(map(int, input().split()))
m_set = set(map(int, input().split()))
result = 0

result += len(n_set - m_set) + len(m_set - n_set)
print(result)

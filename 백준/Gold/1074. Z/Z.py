def z_search(n, r, c):
    if n == 0:
        return 0
    
    # 범위 사등분
    size = 2 ** (n - 1)
    area = size * size # 한 사분면의 크기
    
    # r, c가 어느 사분면에 속하는지 확인
    if r < size and c < size: # 1사분면
        return z_search(n - 1, r, c)
    elif r < size and c >= size: # 2사분면
        return area + z_search(n - 1, r, c - size)
    elif r >= size and c < size: # 3사분면
        return 2 * area + z_search(n - 1, r - size, c)
    else: # 4사분면
        return 3 * area + z_search(n - 1, r - size, c - size)

N, r, c = map(int, input().split())
print(z_search(N, r, c))
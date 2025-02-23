def solve():
    import sys
    input_data = sys.stdin.readline().strip().split()
    N, M, K = map(int, input_data)
    
    answer = min(M, K) + min(N - M, N - K)
    print(answer)

solve()
count = 0
answer = -1

def merge_sort(A, p, r, K):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, K)
        merge_sort(A, q+1, r, K)
        merge(A, p, q, r, K)

def merge(A, p, q, r, K):
    global count, answer
    
    i = p
    j = q + 1
    tmp = []
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
            
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    t = 0
    i = p
    while i <= r:
        A[i] = tmp[t]
        count += 1
        if count == K:
            answer = A[i]
        i += 1
        t += 1

def main():
    global count, answer
    
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    merge_sort(A, 0, N-1, K)
    
    print(answer)

if __name__ == "__main__":
    main()
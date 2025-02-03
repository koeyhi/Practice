import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, (-x, x))
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
            
# https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html heap 개념
# https://littlefoxdiary.tistory.com/3 heapq 모듈 사용법
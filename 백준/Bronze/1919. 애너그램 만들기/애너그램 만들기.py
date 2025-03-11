import sys
from collections import Counter


def solve():
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()

    freqA = Counter(A)
    freqB = Counter(B)

    answer = sum((freqA - freqB).values()) + sum((freqB - freqA).values())
    print(answer)


solve()

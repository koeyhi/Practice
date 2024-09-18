n = int(input())

words = list(set(input() for _ in range(n)))

words.sort(key=lambda x: (len(x), x))  # 튜플을 사용한 다중 기준

for word in words:
    print(word)

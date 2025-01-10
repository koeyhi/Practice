from collections import Counter

n, m = map(int, input().split())
words = []

for _ in range(n):
    word = input()
    if len(word) >= m:
        words.append(word)

word_count = Counter(words)
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)

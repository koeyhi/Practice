from collections import Counter


def char_to_num(c):
    if c == " ":
        return 0
    elif "A" <= c <= "Z":
        return ord(c) - ord("A") + 1
    elif "a" <= c <= "z":
        return ord(c) - ord("a") + 27


N = int(input())
cipher_nums = list(map(int, input().split()))
text = input()

plaintext_nums = [char_to_num(c) for c in text]

cipher_counter = Counter(cipher_nums)
plaintext_counter = Counter(plaintext_nums)

if cipher_counter == plaintext_counter:
    print("y")
else:
    print("n")
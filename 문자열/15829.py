# l = int(input())
# s = input()
# d = {}
# index = 1

# for i in "abcdefghijklmnopqrstuvwxyz":
#     d[i] = index
#     index += 1

# hash_value = sum([d[s[i]] * (31**i) for i in range(l)]) % 1234567891

# print(hash_value)

l = int(input())
s = input()
r = 31
m = 1234567891
hash_value = 0

for i in range(l):
    a = ord(s[i]) - ord("a") + 1  # ord : 문자의 유니코드 번호 반환
    hash_value += a * (r**i)
hash_value %= m

print(hash_value)

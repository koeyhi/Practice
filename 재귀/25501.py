def recursion(s, l, r, count):
    count[0] += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1, count)


def isPalindrome(s):
    count = [0]
    return recursion(s, 0, len(s) - 1, count), count[0]


t = int(input())

for _ in range(t):
    s = input()
    result, count = isPalindrome(s)
    print(result, count)

n = int(input())

for _ in range(n):
    s = input()
    stack = []
    balanced = True

    for p in s:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if stack:
                stack.pop()
            else:
                balanced = False
                break
    if balanced and not stack:
        print("YES")
    else:
        print("NO")

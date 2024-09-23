from collections import deque

while True:
    s = input()
    if s == ".":
        break

    stack = deque()
    balanced = True

    for char in s:
        if char in "([":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                balanced = False
                break
            stack.pop()
        elif char == "]":
            if not stack or stack[-1] != "[":
                balanced = False
                break
            stack.pop()
    if balanced and not stack:
        print("yes")
    else:
        print("no")

# 스택 이용해서 문자열 반복하면서 괄호만 스택에 추가하고,
# 닫는 괄호가 나오는 경우 스택의 가장 뒤 문자가 현재 닫는 괄호와 매치하는 경우 pop 사용하여 빼내고, 아닐 경우 no 출력
# 반복이 종료된 후 balanced 값이 True 이고, 스택이 비어있는 경우 yes 출력

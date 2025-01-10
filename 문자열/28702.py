str_list = []

for _ in range(3):
    str_list.append(input())

for s in str_list:
    if s.isdigit():
        result = int(s) + 3 - str_list.index(s)
        if result % 15 == 0:
            print("FizzBuzz")
        elif result % 3 == 0:
            print("Fizz")
        elif result % 5 == 0:
            print("Buzz")
        else:
            print(result)
        break

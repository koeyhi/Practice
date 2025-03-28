while True:
    s = input()
    if s[-1] == "#":
        break
    elif s[-1] == "e":
        if s.count("1") % 2 == 0:
            print(s[:-1] + "0")
        else:
            print(s[:-1] + "1")
    elif s[-1] == "o":
        if s.count("1") % 2 == 0:
            print(s[:-1] + "1")
        else:
            print(s[:-1] + "0")
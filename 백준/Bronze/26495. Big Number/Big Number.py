n = input()
for i in n:
    x = int(i)
    if x == 0:
        print(
            """0000
0  0
0  0
0  0
0000
"""
        )
    elif x == 1:
        print(
            """   1
   1
   1
   1
   1
"""
        )
    elif x == 2:
        print(
            """2222
   2
2222
2
2222
"""
        )
    elif x == 3:
        print(
            """3333
   3
3333
   3
3333
"""
        )
    elif x == 4:
        print(
            """4  4
4  4
4444
   4
   4
"""
        )
    elif x == 5:
        print(
            """5555
5
5555
   5
5555
"""
        )
    elif x == 6:
        print(
            """6666
6
6666
6  6
6666
"""
        )
    elif x == 7:
        print(
            """7777
   7
   7
   7
   7
"""
        )
    elif x == 8:
        print(
            """8888
8  8
8888
8  8
8888
"""
        )
    else:
        print(
            """9999
9  9
9999
   9
   9
"""
        )
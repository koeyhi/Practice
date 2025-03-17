import sys

N = int(input())

while True:
    for x in range(1, N + 1):
        print(f"? {x}")
        sys.stdout.flush()

        respond = input()

        if respond == "Y":
            print(f"! {x}")
            sys.stdout.flush()
            break
    else:
        continue
    break
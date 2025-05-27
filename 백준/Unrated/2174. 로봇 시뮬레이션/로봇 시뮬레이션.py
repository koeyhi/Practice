import sys

input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())

direction = {"N": 0, "E": 1, "S": 2, "W": 3}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
graph = [[0] * (a + 1) for _ in range(b + 1)]
robots = [None] * (n + 1)

for i in range(1, n + 1):
    x, y, action = input().split()
    x, y = int(x), int(y)
    graph[y][x] = i
    robots[i] = [x, y, direction[action]]

for _ in range(m):
    robot, command, repeat = input().split()
    robot, repeat = int(robot), int(repeat)

    x, y, action = robots[robot]

    if command == "L":
        action = (action - repeat) % 4
        robots[robot][2] = action
    elif command == "R":
        action = (action + repeat) % 4
        robots[robot][2] = action
    else:
        for _ in range(repeat):
            nx = x + dx[action]
            ny = y + dy[action]
            if not (1 <= nx <= a and 1 <= ny <= b):
                print(f"Robot {robot} crashes into the wall")
                exit()
            if graph[ny][nx] != 0:
                print(f"Robot {robot} crashes into robot {graph[ny][nx]}")
                exit()

            graph[y][x] = 0
            graph[ny][nx] = robot
            x, y = nx, ny
        robots[robot][0], robots[robot][1] = x, y

print("OK")
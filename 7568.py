n = int(input())
people = []
rank = [1] * n

for i in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

for i in range(len(people) - 1):
    for j in range(i + 1, len(people)):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1
        elif people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            rank[j] += 1

for i in rank:
    print(i, end=" ")

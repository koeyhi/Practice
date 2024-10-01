angle = [int(input()) for _ in range(3)]
if angle[0] == 60 and angle[1] == 60 and angle[2] == 60:
    print("Equilateral")
elif sum(angle) == 180 and (
    angle[0] == angle[1] or angle[0] == angle[2] or angle[1] == angle[2]
):
    print("Isosceles")
elif sum(angle) == 180:
    print("Scalene")
else:
    print("Error")

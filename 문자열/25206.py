grade_std = {"A+": 4.5,"A0": 4.0,"B+": 3.5,"B0": 3.0,"C+": 2.5,"C0": 2.0,"D+": 1.5,"D0": 1.0,"F": 0.0,}
sum_score, total_score = 0, 0

for _ in range(20):
    _, score, grade = input().split()
    if grade != 'P':
        score = float(score)
        total_score += score
        sum_score += grade_std[grade] * score

print(sum_score / total_score)
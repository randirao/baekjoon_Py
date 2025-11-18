grade_map = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
data = [input().split() for _ in range(20)]
sum = 0
total_score = 0

for subject, score, grade in data:
    if grade == "P":
        continue
    else:
        sum += grade_map[grade] * float(score)
        total_score += float(score)
print('%.6f' % (sum/total_score))
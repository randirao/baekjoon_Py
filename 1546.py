n = int(input())
grade = list(map(int, input().split()))
max_grade = max(grade)
for i in range(n):
    grade[i] = grade[i]/max_grade*100
print(sum(grade)/len(grade))
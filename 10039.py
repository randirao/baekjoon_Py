score = 0
for _ in range(5):
    sco = int(input())
    score += max(sco, 40)
print(score//5)
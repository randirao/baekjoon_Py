s = str(input())
groups = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
sum = 0
for i in s:
    for j in range(len(groups)):
        if i in groups[j]:
            sum += j+3
            break
print(sum)
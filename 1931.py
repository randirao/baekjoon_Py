n = int(input())
lst = []
count = 0
end = 0
for i in range(n) :
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[1], x[0]))
for i in lst :
    if i[0] >= end:
        count += 1
        end = i[1]
print(count)
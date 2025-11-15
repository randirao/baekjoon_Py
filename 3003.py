체스 = list(map(int, input().split()))
lst = [1, 1, 2, 2, 2, 8]
for i in range(len(lst)) :
    print(int(lst[i])-체스[i], end=' ')
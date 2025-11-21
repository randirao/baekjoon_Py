n = int(input())
lst = [[0]*100 for _ in range(100)]
count = 0
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        idx_i = i
        for j in range(b, b+10):
            idx_j = j
            if lst[idx_i][idx_j] == 0:
                lst[idx_i][idx_j] = 1
                count += 1
            else:
                pass
print(count)
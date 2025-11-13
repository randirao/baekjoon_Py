n, m = map(int, input().split())
lst = [idx for idx in range(1, n+1)]

for n in range(m):
    i, j = map(int, input().split())
    if i == j:
        continue
    else:
        lst[i-1:j] = lst[i-1:j][::-1]
print(*lst)
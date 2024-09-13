n, m = map(int, input().split())
p = [0] * (n+1)

for _ in range(m) :
    i, j, k = map(int, input().split())
    for index in range(i, j+1):
        p[index] = k
print(*p[1:])
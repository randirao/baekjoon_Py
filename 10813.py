n, m = map(int, input().split())
p = [i for i in range(n+1)]

for _ in range(m) :
    i, j = map(int, input().split())
    p[i], p[j] = p[j], p[i]

print(*p[1:], end = ' ')
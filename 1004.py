t = int(input())
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for i in range(n) :
        cx, cy, r = map(int, input().split())

# 2 -> t
# -5 1 12 1 -> x1, y1, x2, y2
# 7 -> n
# 1 1 8 -> cx, cy, r
# -3 -1 1 -> cx, cy, r
# 2 2 2 -> cx, cy, r
# 5 5 1 -> cx, cy, r
# -4 5 1 -> cx, cy, r
# 12 1 1 -> cx, cy, r
# 12 1 2 -> cx, cy, r

# -5 1 5 1 -> x1, y1, x2, y2
# 1 -> n
# 0 0 2 -> cx, cy, r
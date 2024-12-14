import sys
sys.setrecursionlimit(10**6)

aX = [0, 0, -1, 1]
aY = [-1, 1, 0, 0]

def f(i, j) :
    arr[i][j] = 0
    for k in range(4) :
        nX = i + aX[k]
        nY = j + aY[k]
        if (0 <= nX < n and 0 <= nY < m) and arr[nX][nY] == 1 :
            f(nX, nY)

t = int(input())
for _ in range(t) :
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k) :
        x, y = map(int, input().split())
        arr[y][x] = 1

    count = 0
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 1 :
                f(i, j)
                count += 1
    print(count)
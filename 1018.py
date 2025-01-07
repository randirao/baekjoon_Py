n, m = map(int, input().split())
arr = [input() for _ in range(n)]
min_cnt = 64

for x in range(n-7):
    for y in range(m-7):
        cnt = 0

        for i in range(x, x+8):
            for j in range(y, y+8):
                if ((i+j) % 2 == 0) and arr[i][j] == 'W':
                    cnt += 1
                elif ((i+j) % 2 != 0) and arr[i][j] == 'B':
                    cnt += 1
        min_cnt = min(min_cnt, cnt, 64-cnt)
print(min_cnt)
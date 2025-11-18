n, m = map(int, input().split())
arr = []
brr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    brr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(arr[i][j] + brr[i][j], end=' ')
    print()
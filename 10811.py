n, m = map(int, input().split())
arr = [i for i in range(1, n+1)] #초기화
tmp = 0
for _ in range(m) : #m번 돌리기
    i, j = map(int, input().split()) #i, j입력
    for k in range(j-1, i-1, -1): #i부터 j까지 돌리기
        print(f"k: {k}")
        tmp = arr[k]
        arr[k] = arr[k-1]
        arr[k-1] = tmp
    print(*arr)


# 1 2 3 4 5
# 1 2 3 5 4
# 1 2 5 3 4
# 1 5 2 3 4
# 5 1 2 3 4
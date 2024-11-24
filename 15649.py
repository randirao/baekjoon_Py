n, m = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(i)
    if arr[i] == m :
        print(arr[i])
    for j in range(n) :
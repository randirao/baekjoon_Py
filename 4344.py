C = int(input())
for i in range(C) :
    data =  list(map(int, input().split()))
    N = data[0]
    data1 = sum(data[1:])
    score = data1/N
    count = 0
    for j in range(N) :
        if data[j+1] > score :
            count += 1
    print(f"{((count / N)*100):.3f}%")

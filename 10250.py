t = int(input())

for i in range(t):
    h,w,n = map(int, input().split()) # 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    cnt = 0 
    floor = 0
    ho = 0

    for k in range(1,w+1):  # 1~w만큼 / 각 층의 방 수
        for j in range(1,h+1):  # 1~h만큼 / 호텔의 층 수
            cnt+=1  # for문이 한번 돌 때마다 cnt 1증가
            if(cnt==n): # cnt가 n과 같으면
                floor = str(j) # 층은 j
                ho = str(k) # 호는 k
    if(int(ho)<10):
        print(floor+"0"+ho)
    else:
        print(floor+ho)
while True :
    a = input()    #120
    if a=='0' :
        break
    else :
        sum = 1 #기본 여백
        for i in a:
            if i == '1':
                sum += 3
            elif i == '0':
                sum += 5
            else :
                sum += 4
        print(sum)
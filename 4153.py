while True :
    a, b, c = map(int, input().split())
    if a==0 and b==0 and c==0 :
        break
    elif a>b and a>c :
        if a*a == b*b + c*c :
            print("right")
        else :
            print("wrong")
    elif b>c and b>a :
        if b*b == a*a + c*c :
            print("right")
        else :
            print("wrong")
    elif c>b and c>a :
        if c*c == b*b + a*a :
            print("right")
        else :
            print("wrong")
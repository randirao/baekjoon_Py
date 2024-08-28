a, b, c = map(int, input().split())

if a == b and b == c :
    print(10000+a*1000)
    
elif a == b or b == c or c == a :
    print(1000+a*100 if a==b or a==c else 1000+b*100)
    
else : 
    print((a*100 if a>c else c*100) if a>b else (b*100 if b>c else c*100))
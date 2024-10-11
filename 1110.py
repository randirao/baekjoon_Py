n = int(input())  #26
c = n #c=26
cnt=0

while True :
    #n=26 / n=68
    a = n%10    #a=6 / a=8
    b = n//10 + a   #b=2+6=8 / b=6+8=14
    if b>9 :
        b %= 10
    n = a*10 + b   #n=60+8=68
    cnt+=1  #cnt=1
    if n==c :
        break
print(cnt)
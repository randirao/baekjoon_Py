n = int(input())  #26
c = n
cnt=0

while True :
    a = n%10    #a=6
    b = n//10+a   #b=2+6=8
    n = a*10 + b   #n=60+8=68
    cnt+=1
    if n==c :
        break
print(cnt)
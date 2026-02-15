n = int(input()) #18
오 = n//5 #18//5=3
count = 0
while 오>=0: #3
    rem = n-5*오 #18-5*3=3
    if rem%3==0: #3%3=0
        삼 = rem//3
        count = 오 + 삼
        break
    오 -= 1
else:
    print(-1)
    exit()
print(count)
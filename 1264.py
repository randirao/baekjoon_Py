listt = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
while True :
    cnt = 0
    a = input()
    if a == "#" :
        break
    for i in a :
        if i in listt :
            cnt += 1
    print(cnt)
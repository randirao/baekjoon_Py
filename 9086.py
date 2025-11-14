n = int(input())
s = [str(input()) for _ in range(n)]
for i in s :
    print(i[0] + i[-1])
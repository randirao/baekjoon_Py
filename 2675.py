t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    for k in s:
        for j in range(r):
            print(k, end='')
    print()
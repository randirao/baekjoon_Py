a, b, c = map(int, input().split())

if a>=b and a>=c:
    if b>=c :
        print(b)
    else :
        print(c)
elif b>=c and b>=a:
    if c>=a :
        print(c)
    else :
        print(a)
elif c>=a and c>=b:
    if a>=b :
        print(a)
    else :
        print(b)
x, y, w, h = map(int, input().split())
if abs(x-0) < abs(w-x):
    a = abs(x-0)
else :
    a = abs(w-x)
if abs(y-0) < abs(h-y) :
    b = abs(y-0)
else :
    b = abs(h-y)

if a < b:
    print(a)
else :
    print(b)
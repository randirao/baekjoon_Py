import sys

s = str(input())
for i in range(len(s)//2+1) :
    if s[i] == s[-i-1] :
        continue
    else:
        print(0)
        sys.exit()
print(1)
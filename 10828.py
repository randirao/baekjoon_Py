import sys

input = sys.stdin.readline
n = int(input())
stack = []
result = []
for i in range(n) :
    x = input().split()
    if x[0] == 'push':
        stack.append(x[1])
    elif x[0] == 'pop':
        if not stack :
            result.append(-1)
        else:
            result.append(stack.pop())
    elif x[0] == 'size':
        result.append(len(stack))
    elif x[0] == 'empty':
        result.append(0 if stack else 1)
    elif x[0] == 'top':
        result.append(-1 if not stack else stack[-1])
print(*result)
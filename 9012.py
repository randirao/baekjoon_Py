t = int(input())
for i in range(t) :
    x = input().strip()
    stack = [ ]
    balanced = "YES"

    for i in x :
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                balanced = "NO"
                break
            top = stack.pop()
            if top == '(':
                continue
    if stack:
        balanced = "NO"
    print(balanced)
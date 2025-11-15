a, b = map(int, input().split())
a = int(str(a)[::-1])
b = int(str(b)[::-1])
print(a if a > b else b)
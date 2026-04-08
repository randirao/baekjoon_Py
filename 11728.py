n, m = map(int, input().split())
a = [int(x) for x in input().split()][:n]
b = [int(x) for x in input().split()][:m]
print(*(sorted(a+b)))
import sys

n = int(input().strip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))[:n]

prefix = [0] * (n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + num[i]

result = []
for _ in range(m):
    a, b = map(int, input().split())
    result.append(str(prefix[b] - prefix[a-1]))
print("\n".join(result))
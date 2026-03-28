import sys

input = sys.stdin.readline
n = int(input())
lst = [0] * 10001
for _ in range(n):
    lst[int(input())] += 1
for i in range(1, 10001):
    if lst[i]:
        for _ in range(lst[i]):
            print(i)
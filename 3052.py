arr = [int(input())%42 for _ in range(10)]
cnt = [0] * 42

for i in arr:
    cnt[i] = 1
print(cnt.count(1))
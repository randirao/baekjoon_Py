x = int(input())
n = int(input())

sum = 0

for i in range(0, n) :
    r_pay, r_cnt = map(int, input().split())
    sum += r_pay*r_cnt
print("Yes" if (sum==x) else "No")
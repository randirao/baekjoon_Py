m, n = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            s = cards[i] + cards[j] + cards[k]
            if s <= n and s > max_sum:
                max_sum = s


print(max_sum)
N = int(input())
first_n = 1
max_n = 1
while max_n < N:
    max_n += first_n * 6
    first_n += 1
print(first_n)
import math

def is_prime(n: int) -> bool:
    if n <2:
        return False
    if n % 2==0:
        return n == 2
    r = math.isqrt(n)
    for i in range(3, int(r)+1, 2):
        if n % i == 0:
            return False
    return True

N = int(input())
n = list(map(int, input().split()))
count = 0

for i in n:
    if is_prime(i):
        count += 1

print(count)
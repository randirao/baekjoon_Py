abc = [int(input()) for i in range(3)]
product = abc[0] * abc[1] * abc[2]
result = list(map(int, str(product)))
count = [0] * 10
for i in range(0, 10):
    for j in result:
        if j == i:
            count[i] += 1
for i in range(10):
    print(count[i])
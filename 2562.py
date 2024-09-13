arr = list()
for i in range(9) :
    arr.append(int(input()))
max = arr[0]
max_index = 0
for i in range(9) :
    if arr[i] > max :
        max = arr[i]
        max_index = i
print(max)
print(max_index + 1)
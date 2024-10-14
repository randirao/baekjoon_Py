n = int(input())
arr = [[None for _ in range(n)] for _ in range(20000)]
min = 20001
max = 0
for i in range(n) :
    arr[i] = input()
    length = len(arr[i]) #length에 arr[i]의 길이 저장
    if length == min or length == max :
        if
    if length < min : #만약 length가 min보다 작으면
        min = length #min에 length 넣기
    if length > max : #length가 max보다 크면
        max = length #max에 length 넣기
arr = [0] *29
arr_check = [0] * 31

#입력받기
for i in range(1, 29):
    arr[i] = int(input())
    #arr[i]를 arr_check[arr[i]]에 담기
    arr_check[arr[i]] = 1

#비어 있는 칸 찾기
for i in range(1, 31):
#     #arr_check[i]가 비어있으면
    if arr_check[i] == 0 :
        print(i)
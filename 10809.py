s = str(input())    # baekjoon 입력
lst = [-1] * 26     # a, b, c, ... , z까지를 -1로 초기화
n = 0   # 몇번째 글자인지 알기 위한 n
for idx, i in enumerate(s) :    # 글자 수만큼 반복
    m = ord(i) - ord('a')   # 변수 m은 i번째 글자를 숫자로 변환하여 a를 숫자로 변환한 97만큼 뺀 값
    if lst[m] != -1 :
        n += 1
        continue
    elif lst[m] == -1 :
        lst[m] = n
        n += 1
print(*lst)
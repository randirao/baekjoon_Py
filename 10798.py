str = [input() for _ in range(5)]
max_len = len(max(str, key=len))

for i in range(max_len):
    for j in range(5):
        if i < len(str[j]):
            print(str[j][i], end="")
        else:
            continue
s = input()
count = [0]*26
for i in range(len(s)):
    count[ord(s[i])-97] += 1
print(' '.join(map(str, count)))
n = int(input())
count = 0
for i in range(n):
    s = str(input())
    seen = set()
    prev = s[0]
    seen.add(prev)
    isGrouped = True
    for j in range(0, len(s)):
        if s[j] == prev:
            continue
        else:
            if s[j] not in seen:
                prev = s[j]
                seen.add(prev)
            else:
                isGrouped = False
                break
    if isGrouped:
        count += 1
print(count)
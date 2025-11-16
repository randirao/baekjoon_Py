s = str(input()).lower()
lst = [s.count(chr(i)) for i in range(97, 123)]
print('?' if lst.count(max(lst)) != 1 else chr(lst.index(max(lst))+65))
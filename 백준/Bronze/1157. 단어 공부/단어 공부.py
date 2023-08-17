sent = input().upper()
L = [0 for i in range(26)]
for i in sent :
    L[ord(i)-65] += 1

tmp = max(L)
if L.count(tmp) > 1 :
    print("?")
else :
    print("%s"%chr(L.index(tmp)+65))
word = input()
i = 0
cnt = 0
while i < len(word) :
    cnt += 1
    if i+1 < len(word) and word[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="] :
        i += 2
    elif i+2 < len(word) and word[i:i+3] == "dz=" :
        i += 3
    else :
        i += 1
    
print(cnt)
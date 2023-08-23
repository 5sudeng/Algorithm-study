M = int(input())
N = int(input())

L = []

def prime(num) :
    isP = 0
    if num > 5 :
        for i in range(2, num//2) :
            if num%i == 0 :
                isP = 0
                break
            isP = 1
    elif (num!=1) and (num!=4):
        isP = 1
    return isP
  
for i in range(M, N+1) :
    if prime(i) :
        L.append(i)
        
if len(L) == 0 :
    print("-1")
else :
    print(sum(L))
    print(min(L))
        
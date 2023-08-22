import sys
n = int(input())
L = []
for i in range(n) :
    t = tuple(map(int, sys.stdin.readline().split()))
    L.append(t)
    
L.sort(key = lambda x : (x[0],x[1]))

for i in range(n) :
    print(L[i][0], L[i][1])
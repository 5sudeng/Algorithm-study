import sys
k = int(sys.stdin.readline())
array = []
for i in range(k) :
    x = int(input())
    if x == 0 :
        array.pop()
        continue
    array.append(x)
    
print(sum(array))
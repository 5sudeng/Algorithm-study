import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))

cost = p[0]
result = 0

for i in range(n-1) :
    if cost > p[i] :
        cost = p[i]
    result += l[i]*cost
print(result)
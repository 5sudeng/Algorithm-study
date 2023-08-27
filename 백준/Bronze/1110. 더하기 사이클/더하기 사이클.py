n = int(input())

tmp = n
cnt = 0

while True :
    tmp = ((tmp//10)+(tmp%10))%10 + (tmp%10)*10
    cnt += 1
    if tmp == n :
        break

print(cnt)
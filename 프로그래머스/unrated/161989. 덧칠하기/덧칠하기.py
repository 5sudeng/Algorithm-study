def solution(n, m, section):
    answer = 0
    cur = 0
    for i in section :
        if i < cur :
            continue
        if cur > n :
            break
        cur = i + m
        answer += 1
        
    return answer
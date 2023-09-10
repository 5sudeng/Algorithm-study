def solution(wallpaper):
    n, m = len(wallpaper), len(wallpaper[0])
    xs, ys = [], []
    for i in range(n) :
        '''if "#" not in i :
            continue'''
        for j in range(m) :
            if wallpaper[i][j] == "#" :
                xs.append(i)
                ys.append(j)
    
    answer = [min(xs), min(ys), max(xs)+1, max(ys)+1]
    return answer
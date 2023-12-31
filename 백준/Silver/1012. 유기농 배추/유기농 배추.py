from collections import deque
import sys
t = int(sys.stdin.readline())
result = [0 for _ in range(t)]
for idx in range(t) :
    m, n, k = map(int, sys.stdin.readline().split())
    pos = [list(map(int, sys.stdin.readline().split())) for i in range(k)]

    graph = [[0 for _ in range(m)] for _ in range(n)] 

    for i, j in pos :
        graph[j][i] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y) :
        queue = deque()
        queue.append((x, y))
        while queue :
            x, y = queue.popleft()
            if graph[x][y] == 0 :
                continue
            graph[x][y] = 0
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 0 :
                    continue
                queue.append((nx, ny))
    
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 0 :
                continue
            bfs(i, j)
            result[idx] += 1


for i in result :
    print(i)
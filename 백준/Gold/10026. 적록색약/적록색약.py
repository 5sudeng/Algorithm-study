import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline()[:-1]) for _ in range(n)]
graph2 = [g[:] for g in graph]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def countRG(x, y, count) :
    graph[x][y] = count
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>= n :
                continue
            if graph[nx][ny] == "R" or graph[nx][ny] == "G" :
                graph[nx][ny] = count
                queue.append((nx, ny))

def countR(x, y, count) :
    graph[x][y] = count
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>= n :
                continue
            if graph[nx][ny] == "R" :
                graph[nx][ny] = count
                queue.append((nx, ny))


def countG(x, y, count) :
    graph[x][y] = count
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>= n :
                continue
            if graph[nx][ny] == "G" :
                graph[nx][ny] = count
                queue.append((nx, ny))

def countB(x, y, count) :
    graph[x][y] = count
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>= n :
                continue
            if graph[nx][ny] == "B" :
                graph[nx][ny] = count
                queue.append((nx, ny))

result = []
count = 0
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == "R" :
            countR(i, j, count)
            count += 1
        elif graph[i][j] == "G" :
            countG(i, j, count)
            count += 1
        elif graph[i][j] == "B" :
            countB(i, j, count)
            count += 1
        else :
            continue

result.append(count)
count = 0
graph = graph2
for i in range(n) :
    for j in range(n) :
        if graph[i][j] in ["R", "G"] :
            countRG(i, j, count)
            count += 1
        elif graph[i][j] == "B" :
            countB(i, j, count)
            count += 1
        else :
            continue
result.append(count)

print(result[0], result[1])
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(n)]


q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



max_v = 0
for i in range(n):
    if max_v < max(graph[i]):
        max_v = max(graph[i])



rain = 0


def BFS(rain):
    danji = 0
    visited = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and visited[i][j] == -1:
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    x, y = q.popleft()
                    

                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if nx<0 or ny<0 or nx>=n or ny>=n:
                            continue
                        if visited[nx][ny] != -1:
                            continue
                        if graph[nx][ny] <= rain:
                            continue
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                danji += 1
    
    
            
    return danji

ans = 0
while 1:
    danji = BFS(rain)
    if rain >= max_v:
        break
    
    
    

    if ans < danji:
        ans = danji
    rain += 1

print(ans)





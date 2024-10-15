import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(m)]
visited = [[-1]*n for _ in range(m)]

dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
q = deque()

def BFS(i, j):
    q.append((i, j))
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if visited[nx][ny] != -1:
                continue
            if graph[nx][ny] != 1:
                continue
            q.append((nx, ny))
            visited[nx][ny] = 1
        

danji = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] != 1:
            BFS(i, j)
            danji += 1

print(danji)
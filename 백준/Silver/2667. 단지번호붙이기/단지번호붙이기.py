import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip())
graph = [input().strip() for _ in range(n)]
visited = [[-1]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == "0":
                continue
            if visited[nx][ny] != -1:
                continue
            visited[nx][ny] = 1
            q.append((nx, ny))
            cnt += 1
    return cnt

ans = []
danji = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == "1" and visited[i][j] == -1:
            ans.append(BFS(i, j))
            danji += 1
ans.sort()
print(danji)
print("\n".join(list(map(str, ans))))
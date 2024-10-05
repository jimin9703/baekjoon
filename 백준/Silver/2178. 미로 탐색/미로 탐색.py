import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [input().strip() for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
q = deque()
q.append((0, 0))
visited[0][0] = 1

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>= m:
            continue
        if graph[nx][ny] == "0":
            continue
        if visited[nx][ny] != -1:
            continue
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))

print(visited[n-1][m-1])
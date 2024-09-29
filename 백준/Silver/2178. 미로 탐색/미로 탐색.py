import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = list(input().strip() for _ in range(n))
visited = [[-1] * m for _ in range(n)]
q = deque()
q.append((0,0))
visited[0][0]=1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
    qx, qy = q.popleft()
    for i in range(4):
        nx, ny = qx + dx[i], qy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == "0":
            continue
        if visited[nx][ny] != -1:
            continue
        visited[nx][ny] = visited[qx][qy] + 1
        q.append((nx, ny))
        
print(visited[n-1][m-1])
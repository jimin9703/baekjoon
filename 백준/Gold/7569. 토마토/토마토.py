import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().strip().split())
graph = [[input().strip().split() for _ in range(n)] for _ in range(h)]
visited = [[[-1]*m for _ in range(n)] for _ in range(h)]

q = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == "1":
                q.append((i, j, k))

nxt = []
cnt = 0

while q:
    qz, qx, qy = q.popleft()

    for i in range(6):
        nz, nx, ny = qz + dz[i], qx + dx[i], qy + dy[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
            continue
        if graph[nz][nx][ny] != "0":
            continue
        if visited[nz][nx][ny] != -1:
            continue
        visited[nz][nx][ny] = 1
        graph[nz][nx][ny] = "1"
        nxt.append((nz, nx, ny))
    if not q and nxt:
        cnt += 1
        while nxt:
            q.append(nxt.pop())


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == "0":
                print(-1)
                exit(0)

print(cnt)
import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(m)]
visited = [-1] * (n+1)
q = deque()
q.append(1)
visited[1] = 1

while q:
    x = q.popleft()
 
    for i in range(m):
        if graph[i][0] == x:
            nx = graph[i][1]
            if visited[nx] != -1:
                continue
            visited[nx] = 1
            q.append(nx)
        if graph[i][1] == x:
            nx = graph[i][0]
            if visited[nx] != -1:
                continue
            visited[nx] = 1
            q.append(nx)

cnt = 0
for i in range(n+1):
    if visited[i] == 1:
        cnt += 1

print(cnt-1)
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().strip().split())
    graph[b].append(a)


q = deque()

def BFS(start):
    q.append(start)
    visited = [-1]*(n+1)
    visited[start] = 1
    cnt = 0
    
    while q:
        x = q.popleft()

        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = 1
                q.append(i)
                cnt += 1
    return cnt
max_v = 0
ans = [0]*(n+1)
for i in range(1, n+1):
    count = BFS(i)
    ans[i] = count

    if count >= max_v:
        max_v = count

for i in range(1, n+1):
    if ans[i] == max_v:
        print(i, end=" ")
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().strip().split())
visited = [INF] * 100001
q = deque()
q.append(n)
visited[n] = 0

while q:
    x = q.popleft()

    for i in [x*2, x+1, x-1]:
        if 0 <= i and i <= 100000:
            if visited[i] >= visited[x]+1:
                visited[i] = visited[x] + 1
                q.append(i)

print(visited[k])

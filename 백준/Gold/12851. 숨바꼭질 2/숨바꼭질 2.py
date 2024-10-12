import sys
from collections import deque
input = sys.stdin.readline
INF= int(9e18)
q = deque()

n, k = map(int, input().strip().split())
visited = [INF] * 100001
q.append(n)
visited[n] = 0
cnt = 0
ans = []

while q:
    x = q.popleft()

    for i in [x*2, x+1, x-1]:
        if 0<=i and i<=100000:
            if visited[i] >= visited[x]+1:
                visited[i] = visited[x]+1
                q.append(i)

        if i == k:
            if visited[i] == visited[x]+1:
                cnt += 1
                


print(visited[k])

if n == k:
    cnt = 1
print(cnt)
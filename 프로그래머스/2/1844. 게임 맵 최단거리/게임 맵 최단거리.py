from collections import deque

def solution(maps):
    q = deque()
    n = len(maps)
    m = len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if maps[nx][ny] == 0:
                continue
            if visited[nx][ny] != -1:
                continue
            visited[nx][ny] = visited[x][y]+1
            q.append((nx, ny))
            
            
    answer = visited[n-1][m-1]
    return answer
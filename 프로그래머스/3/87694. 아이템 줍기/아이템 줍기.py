from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    q = deque()
    graph = [[-1]*102 for _ in range(102)]
    
    for i in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, i)
        for j in range(x1, x2+1):
            for k in range(y1, y2+1):
                if x1<j<x2 and y1<k<y2:
                    graph[j][k] = 0
                elif graph[j][k] != 0:
                    graph[j][k] = 1
                    
    visited = [[-1]*102 for _ in range(102)]
    q.append((characterX*2,characterY*2))
    visited[characterX*2][characterY*2] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        
        if x == itemX*2 and y == itemY*2:
            answer = visited[x][y] // 2
            break
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=102 or ny>=102:
                continue
            if visited[nx][ny] != -1:
                continue
            if graph[nx][ny] != 1:
                continue
            # if graph[nx][ny] == 1 and visited[nx][ny] == -1:
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
                    
    return answer
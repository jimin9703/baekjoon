from collections import deque

def solution(n, computers):
    q = deque()
    visited = [-1] * n

    q.append(0)
    visited[0] = 1
    cnt = 0
    
    while q:
        x = q.popleft()
        
        
        for i in range(1, n):
            if i == x:
                continue
            if visited[i] != -1:
                continue
            if computers[x][i] == 1:
                q.append(i)
                visited[i] = 1
                
        if not q:
            cnt += 1
            for i in range(n):
                if visited[i] == -1:
                    q.append(i)
                    visited[i] = 1
                    break
    answer = cnt
    return answer
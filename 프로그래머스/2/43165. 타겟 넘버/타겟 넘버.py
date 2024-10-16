from collections import deque

def solution(numbers, target):
    q = deque()
    for i in [numbers[0], -numbers[0]]:
        q.append(i)
    cnt = 0
    i = 1
    time = 1
    while q:
        
        x = q.popleft()
        

        for j in [numbers[i], -numbers[i]]:
            nx = x+j

            if nx == target and i == len(numbers) - 1:
                cnt += 1
            else:
                q.append(nx)
        
        if time == 2**i:
            i += 1
            time = 1
        else:
            time += 1
        
        
        if i > len(numbers) - 1:
            break
        
    answer = cnt
    return answer
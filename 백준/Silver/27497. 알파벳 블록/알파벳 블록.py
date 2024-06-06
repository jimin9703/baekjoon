from collections import deque
import sys

d = deque()
n = int(sys.stdin.readline())
li = []

for i in range(n):
    b = list(sys.stdin.readline().strip().split())
    
    if b[0] == '1':
        d.append(b[1])
        li.append(b[0])
    elif b[0] == '2':
        d.appendleft(b[1])
        li.append(b[0])
    elif b[0] == '3':
        if len(d) == 0:
            pass
        else:
            if li[-1] == '1':
                d.pop()
                li.pop()

            elif li[-1] == '2':
                d.popleft()
                li.pop()
                

print("".join(d) if d else 0) # d에 값이 없을 때 0을 출력하는 조건문
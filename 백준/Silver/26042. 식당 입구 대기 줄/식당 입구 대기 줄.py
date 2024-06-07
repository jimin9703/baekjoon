from collections import deque
import sys

n = int(sys.stdin.readline().strip())
d = deque()
max_line = 0
s = 0

for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    if line[0] == 1:
        d.append(line[1])
        if max_line < len(d):
            max_line = len(d)
            s = d[-1]
        elif max_line == len(d):
            if s > d[-1]:
                s = d[-1]

    elif line[0] == 2:
        d.popleft()

print(f"{max_line} {s}")
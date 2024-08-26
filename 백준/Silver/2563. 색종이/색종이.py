import sys

n = int(sys.stdin.readline().strip())

M = [[0] * 100 for _ in range(100)]

for k in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            M[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        cnt += M[i][j]

print(cnt)
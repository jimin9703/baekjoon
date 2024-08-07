import sys

n, m = map(int, sys.stdin.readline().strip().split())

li = [0] * n

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    for j in range(a-1,b):
        li[j] = c

print(*li)
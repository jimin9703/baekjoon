import sys

n, m = map(int, sys.stdin.readline().strip().split())

li = [x for x in range(1,n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    li[a-1:b] = li[a-1:b][::-1]


print(*li)
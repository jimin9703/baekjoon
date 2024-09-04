import sys

n = int(sys.stdin.readline().strip())
L = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

L.sort()
for i in range(n):
  print(*L[i])
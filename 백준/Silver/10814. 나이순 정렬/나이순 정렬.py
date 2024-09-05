import sys

input = sys.stdin.readline

n = int(input().strip())

L = [list(input().strip().split()) + [i] for i in range(n)]

L.sort(key= lambda x : (int(x[0]), x[2]))
for i in range(n):
    print(*L[i][0:2])
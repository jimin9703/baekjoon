import sys

n = int(sys.stdin.readline().strip())

L = [int(sys.stdin.readline().strip()) for _ in range(n)]

L.sort()
print(*L, sep="\n")
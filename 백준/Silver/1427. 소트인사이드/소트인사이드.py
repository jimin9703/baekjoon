import sys

L = list(map(int, sys.stdin.readline().strip()))

L.sort()

L = reversed(L)

print(*L, sep="")
import sys

n = int(sys.stdin.readline().strip())

L = [sys.stdin.readline().strip() for _ in range(n)]
L = set(L)
L = list(L)
L.sort(key=lambda x: (len(x), x))

print(*L, sep="\n")
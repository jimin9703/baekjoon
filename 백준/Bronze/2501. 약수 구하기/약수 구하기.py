import sys

n, k = map(int, sys.stdin.readline().strip().split())

L = []
i = 1

while True:
    if n % i == 0:
        L.append(i)
    if n == i:
        break
    i += 1

if len(L) < k:
    print(0)
else:
    print(L[k-1])
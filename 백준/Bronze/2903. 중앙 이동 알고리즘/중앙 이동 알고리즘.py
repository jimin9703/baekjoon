import sys

n = int(sys.stdin.readline().strip())

L = [0] * 16

for i in range(n+1):
    L[0] = 2
    if i > 0:
        L[i] = L[i-1] * 2 - 1

print(L[n] ** 2)
import sys

n, m = map(int, sys.stdin.readline().strip().split())

L = list(map(int, sys.stdin.readline().strip().split()))

s = 0
A = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            s = L[i] + L[j] + L[k]
            if s <= m:
                A.append(s)

print(max(A))
import sys

b, n = map(int, sys.stdin.readline().strip().split())
a = b
L = []

while True:
    L.append(a % n)
    a = a // n
    if a < n:
        L.append(a)
        break

while L[-1] == 0:
    L.pop()

L.reverse()

for i in range(len(L)):
    if L[i] >= 10:
        L[i] = chr(L[i] + 55)



print(*L, sep="")
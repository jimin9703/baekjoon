import sys

L = [int(sys.stdin.readline().strip()) for _ in range(5)]

L.sort()

m = sum(L) // 5
print(m)
print(L[2])
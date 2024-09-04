import sys

n, k = map(int, sys.stdin.readline().strip().split())

L = list(map(int, sys.stdin.readline().strip().split()))

L.sort()

print(L[-k])
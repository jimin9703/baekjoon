import sys

n = int(sys.stdin.readline().strip())

m = list(map(int, sys.stdin.readline().strip().split()))

print(min(m), max(m))
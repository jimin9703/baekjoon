import sys

a, b = map(int, sys.stdin.readline().strip().split())
c = int(sys.stdin.readline().strip())
d = int(sys.stdin.readline().strip())

if a*d + b <= c*d and c >= a:
    print(1)
else:
    print(0)
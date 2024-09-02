import sys

a, b, c = map(int, sys.stdin.readline().strip().split())

if a >= b + c:
    a = b + c - 1
elif b >= a + c:
    b = a + c - 1
elif c >= b + a:
    c = a + b - 1

l = a + b + c
print(l)
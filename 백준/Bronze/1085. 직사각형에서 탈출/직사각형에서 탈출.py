import sys

x, y, w, h = map(int, sys.stdin.readline().strip().split())

if x < w:
    a = min(w-x, x)
else:
    a = min(x-w, x)

if y < h:
    b = min(h-y, y)
else:
    b = min(y-h, y)

print(min(a, b))
import sys

h, m = map(int, sys.stdin.readline().strip().split())

if m < 45:
    m = m + 15
    if h == 0:
        h = 23
    else:
        h = h - 1
    print(h, m)

else:
    print(h, m-45)


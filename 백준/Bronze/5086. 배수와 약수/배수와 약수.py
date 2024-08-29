import sys

while True:
    n, m = map(int, sys.stdin.readline().strip().split())

    if n == 0 and m == 0:
        exit(0)

    if m % n == 0:
        print("factor")
    elif n % m == 0:
        print("multiple")
    else:
        print("neither")
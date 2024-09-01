import sys

while 1:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a+b+c == 0:
        exit(0)

    if a+b <= c or a+c <= b or b+c <= a:
        print("Invalid")
    elif a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
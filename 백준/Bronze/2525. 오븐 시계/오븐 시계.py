import sys

H, M = map(int, sys.stdin.readline().strip().split())
c = int(sys.stdin.readline().strip())

if c >= 60:
    if M + (c%60) >= 60:
        if H + (c//60) + 1 < 24:
            print(H + (c//60) + 1, M + (c%60) - 60)
        elif H + (c//60) + 1 >= 24:
            print(H + (c//60) - 23, M + (c%60) - 60)
    else:
        if H + (c//60) < 24:
            print(H + (c//60), M + (c%60))
        elif H + (c//60) >= 24:
            print(H + (c//60) - 24, M + (c%60))
else:
    if M + c >= 60:
        if H == 23:
            print(0, M + c - 60)
        else:
            print(H + 1, M + c - 60)
    else:
        print(H, M + c)
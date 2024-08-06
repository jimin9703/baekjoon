import sys

H, M = map(int, sys.stdin.readline().strip().split())

if M > 45:
    print(H, M-45)
elif M == 45:
    print(H, 0)
elif M < 45:
    if H > 0:
        print(H-1, M+15)
    elif H == 0:
        print(23, M+15)
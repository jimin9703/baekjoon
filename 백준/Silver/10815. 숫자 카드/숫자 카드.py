import sys

n = int(sys.stdin.readline().strip())
N = set(map(int,sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
M = list(map(int, sys.stdin.readline().strip().split()))

for i in range(len(M)):
    if M[i] in N:
        M[i] = 1
    else:
        M[i] = 0
print(*M)
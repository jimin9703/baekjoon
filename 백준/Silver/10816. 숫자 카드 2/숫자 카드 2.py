import sys

n = int(sys.stdin.readline().strip())

N = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())

M = list(map(int, sys.stdin.readline().strip().split()))

dict = {}

for i in range(n):
    if N[i] not in dict:
        dict[N[i]] = 1
    else:
        dict[N[i]] += 1

for i in range(m):
    if M[i] not in dict:
        print(0, end=" ")
    else:
        print(dict[M[i]], end=" ")
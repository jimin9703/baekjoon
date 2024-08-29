import sys

n = int(sys.stdin.readline().strip())

m = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0

for i in range(len(m)):
    L = []
    for j in range(1,m[i]+1):
        if not m[i] % j:
            L.append(i)
    if len(L) == 2:
        cnt += 1

print(cnt)
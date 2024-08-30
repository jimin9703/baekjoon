import sys

n = int(sys.stdin.readline().strip())

m = int(sys.stdin.readline().strip())

L = []

for i in range(n, m+1):
    if i == 1:
        continue

    for j in range(2, i):
        if not i % j:
            break
    else:
        L.append(i)

if L:
    print(sum(L))
    print(min(L))
else:
    print(-1)

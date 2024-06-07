import sys

n = int(sys.stdin.readline().strip())

b = list(map(int, sys.stdin.readline().strip().split()))
b.sort()

li = []

for i in range(n):
    if b[i] not in li:
        li.append(b[i])
    else:
        pass

for j in range(len(li)):
    print(li[j], end=" ")
import sys

X = {}
Y = {}

for i in range(3):
    x, y = map(int, sys.stdin.readline().strip().split())

    if x not in X:
        X[x] = 1
    else:
        X[x] += 1
    if y not in Y:
        Y[y] = 1
    else:
        Y[y] += 1

for i in X:
    if X[i] == 1:
        print(i, end=" ")
for i in Y:
    if Y[i] == 1:
        print(i, end=" ")
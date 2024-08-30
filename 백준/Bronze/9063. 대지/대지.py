import sys

n = int(sys.stdin.readline().strip())

X = []
Y = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    X.append(x)
    Y.append(y)

x = max(X) - min(X)
y = max(Y) - min(Y)

print(x*y)

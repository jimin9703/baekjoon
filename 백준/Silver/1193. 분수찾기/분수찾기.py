import sys

n = int(sys.stdin.readline().strip())

L = [0] * 10000
L[0] = 0
L[1] = 1
i = 2

while True:
    L[i] = L[i-1] + i - 1
    if n < L[i]:
        break
    i += 1

n = n - L[i-1]
a = 1+n
b = i-1-n

if i % 2 == 0:
    print(b,"/",a, sep="")
else:
    print(a,"/",b, sep="")
import sys

n = int(sys.stdin.readline().strip())

L = [0] * 100000
L[0] = 1
L[1] = 2
cnt = 1
i = 2

if n == 2:
    cnt = 2

while n > 2:
    L[i] = L[i-1] + 6 * (i-1)
    cnt += 1
    if n < L[i]:
        break
    i += 1

print(cnt)
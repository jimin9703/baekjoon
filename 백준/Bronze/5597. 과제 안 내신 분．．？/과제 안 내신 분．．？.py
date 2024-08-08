import sys

li = [0] * 30

for i in range(28):
    n = int(sys.stdin.readline().strip())
    li[n-1] = n

for i in range(30):
    if li[i] == 0:
        print(i+1)

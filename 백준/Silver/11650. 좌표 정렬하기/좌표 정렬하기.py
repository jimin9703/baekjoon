import sys

n = int(sys.stdin.readline().strip())
li = []

for i in range(n):
    b = list(map(int, sys.stdin.readline().strip().split()))
    li.append(b)

li.sort()

for j in range(len(li)):
    print(li[j][0], li[j][1])
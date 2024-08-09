import sys

li = list(map(int, sys.stdin.readline().strip().split()))
chess = [1, 1, 2, 2, 2, 8]

for i in range(len(li)):
    li[i] = chess[i] - li[i]

print(*li)
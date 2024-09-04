import sys

n = int(sys.stdin.readline().strip())

cnt = [0] * 10001

for i in range(n):
    a = int(sys.stdin.readline().strip())
    cnt[a] += 1

for i in range(1, 10001):
    if cnt[i]:
        for j in range(cnt[i]):
            print(i)
import sys

s = sys.stdin.readline().strip()
n = sys.stdin.readline().strip()

cnt = 0

for i in range(len(n)):
    cnt += int(n[i])


print(cnt)
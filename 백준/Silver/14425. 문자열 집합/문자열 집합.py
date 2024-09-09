import sys

n, m = map(int, sys.stdin.readline().strip().split())

S = [sys.stdin.readline().strip() for _ in range(n)]
M = [sys.stdin.readline().strip() for _ in range(m)]

S = set(S)
cnt = 0

for i in M:
    if i in S:
        cnt += 1

print(cnt)
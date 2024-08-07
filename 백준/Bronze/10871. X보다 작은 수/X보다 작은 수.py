import sys

n, x = map(int, sys.stdin.readline().strip().split())

li_n = list(map(int, sys.stdin.readline().strip().split()))

ans = []

for i in range(n):
    if li_n[i] < x:
        ans.append(li_n[i])


print(*ans)
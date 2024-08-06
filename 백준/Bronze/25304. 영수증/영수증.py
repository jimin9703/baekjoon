import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
ans = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    ans += a*b

if n == ans:
    print("Yes")
else:
    print("No")
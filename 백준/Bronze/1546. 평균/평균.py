import sys

n = int(sys.stdin.readline().strip())

li = list(map(int, sys.stdin.readline().strip().split()))
ans = 0

for i in range(len(li)):
    s = li[i] / max(li) * 100
    ans += s

print(ans / len(li))
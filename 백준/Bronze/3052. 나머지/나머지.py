import sys

li = set()
cnt = 0

for i in range(10):
    n = int(sys.stdin.readline().strip())
    m = n % 42
    li.add(m)

for i in range(len(li)):
    cnt += 1

print(cnt)
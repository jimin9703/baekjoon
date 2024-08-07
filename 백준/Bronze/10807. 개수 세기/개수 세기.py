import sys

n = int(sys.stdin.readline().strip())
li_n = list(map(int, sys.stdin.readline().strip().split()))
v = int(sys.stdin.readline().strip())

count = 0

for i in range(len(li_n)):
    if li_n[i] == v:
        count += 1

print(count)
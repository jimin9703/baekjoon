import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    m = sys.stdin.readline().strip()
    print(m[0],m[-1], sep="")
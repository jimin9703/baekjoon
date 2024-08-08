import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    s = sys.stdin.readline().strip().split()
    for j in range(len(s[1])):
        print(s[1][j]*int(s[0]), end="")
    print()

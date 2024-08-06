import sys

n = int(sys.stdin.readline().strip())
a = 1

for i in range(2,n+1):
    a += i
    
print(a)
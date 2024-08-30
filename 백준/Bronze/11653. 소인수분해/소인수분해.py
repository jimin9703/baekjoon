import sys

n = int(sys.stdin.readline().strip())
m = n
i = 2
while n > 1:
    if m % i:
        i += 1
        
    else:
        print(i)
        m = m / i

    if i > m:
        break
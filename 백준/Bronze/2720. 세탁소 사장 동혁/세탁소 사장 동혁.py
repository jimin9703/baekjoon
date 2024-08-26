import sys

n = int(sys.stdin.readline().strip())



for i in range(n):
    m = int(sys.stdin.readline().strip())
    L = []
    
    L.append(m // 25)
    m = m % 25
    L.append(m // 10)
    m = m % 10
    L.append(m // 5)
    m = m % 5
    L.append(m // 1)

    print(*L, sep=" ")
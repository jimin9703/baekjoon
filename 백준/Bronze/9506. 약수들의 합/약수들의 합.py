import sys

while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        exit(0)
    L = []
    i = 1
    s = 0

    while True:
        if n == i:
            break
        if n % i == 0:
            L.append(i)
        i += 1
    
    for j in range(len(L)):
        s += L[j]
    
    if s == n:
        print(n, "=", end=" ")
        print(*L, sep=" + ")
    else:
        print(n, "is NOT perfect.")

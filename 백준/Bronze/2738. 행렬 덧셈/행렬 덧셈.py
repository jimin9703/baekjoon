import sys

N, M = map(int, sys.stdin.readline().strip().split())


A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]


for i in range(N):
    C = []
    for j in range(M):
        S = A[i][j] + B[i][j]
        C.append(S)
        
    print(*C)


    
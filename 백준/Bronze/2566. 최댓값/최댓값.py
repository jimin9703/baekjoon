import sys

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]

li = []

for i in range(9):
    m = max(arr[i])
    li.append(m)
    
n = max(li)
print(max(li))

for j in range(9):
    for k in range(9):
        if arr[j][k] == n:
            print(j+1, k+1)
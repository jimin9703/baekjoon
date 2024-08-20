import sys

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]

Max = -1
x, y = -1, -1

for i in range(9):
    for j in range(9):
        if arr[i][j] > Max:
            Max = arr[i][j]
            x, y = i, j

print(Max)
print(x+1, y+1)
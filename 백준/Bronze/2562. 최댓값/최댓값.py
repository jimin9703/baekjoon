import sys

li = []

for i in range(9):
    n = int(sys.stdin.readline().strip())
    li.append(n)

m =max(li)
print(m)

for i in range(9):
    if m == li[i]:
        print(i+1)
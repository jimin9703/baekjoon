import sys

arr =list(map(int, sys.stdin.readline().strip().split()))
n = int(sys.stdin.readline().strip())
li = []
a = arr[0]
b = arr[1]
num = 9999

if b-a < 0:
    li.append(a-b)
else:
    li.append(b-a)

for i in range(n):
    c = int(sys.stdin.readline().strip())
    if b-c < 0:
        li.append(c-b)
    else:
        li.append(b-c)

for j in range(n+1):
    if num > li[j]:
        if j == 0:
            num = li[j]
        else:
            num = li[j] + 1

print(num)

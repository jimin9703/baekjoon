import sys

m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
li = [False] * 10001
sum = 0
lin = []

for i in range(m,n+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break

    else:
        li[i] = True
        lin.append(i)

for k in range(m, n+1):
    if li[k] == True:
        sum += k



if sum == 0:
    print(-1)
else:
    print(sum)
    print(lin[0])
import sys

li = list(map(int, sys.stdin.readline().strip().split()))
n = li[0]
k = li[1]

a = [True] * (n+1)
a[0] = [False]
a[1] = [False]
count = 0
ans = 0
flag = 0

for i in range(2, n+1):

    for j in range(i, n+1, i):
        if a[j] == False:
            continue
        a[j] = False
        count += 1

        if count == k:
            flag = True
            ans = j
            break
    if flag == True:
        break

print(ans)
    

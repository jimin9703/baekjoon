import sys

n = int(sys.stdin.readline().strip())

num = list(map(int, sys.stdin.readline().strip().split()))
count = 0

for i in num:
    if i == 1:
        continue

    for j in range(2, i):
        
        if i % j == 0:
            break
    else:
        count += 1

           
print(count)

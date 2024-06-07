import sys

n = int(sys.stdin.readline().strip())
li = []
count = 0
for i in range(n):
    b = list(map(int, sys.stdin.readline().strip().split()))
    li.append(b)
# print(li)
li.sort()
count += (li[0][0] + li[0][1])
for j in range(1, len(li)):
    if count < li[j][0]:
        count = (li[j][0] + li[j][1])
    elif count >= li[j][0]:
        count += li[j][1]

print(count)
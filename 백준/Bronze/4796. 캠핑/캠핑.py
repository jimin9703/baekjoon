import sys

li = []


while 1 :
    count = 0
    num = list(map(int, sys.stdin.readline().split()))
    l = num[0]
    p = num[1]
    v = num[2] 
    # print(l)
    # print(p)
    # print(v)

    if l == 0 and p == 0 and v == 0:
        break

    count += v//p * l

    if (v%p) <= l:
        count += (v%p)
    elif (v%p) > l:
        count += l

    li.append(count)

    

for i in range(len(li)):
    print(f"Case {i+1}:",li[i])


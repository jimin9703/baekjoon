import sys

n = int(sys.stdin.readline().strip())
li = []
num = 1
pic = []
m = 0
flag = False

for i in range(n):
    b = int(sys.stdin.readline().strip())
    mm = m + 1

    if len(li) > 0:
        if b < li[-1]:
            flag = True
            
        elif b == li[-1]:
            li.pop()
            pic.append("-")

        elif b > li[-1]:
            
            while mm <= b:
                li.append(mm)
                pic.append("+")
                mm += 1
            li.pop()
            pic.append("-")
        
                
    elif len(li) == 0:
        
        while mm <= b:
            li.append(mm)
            pic.append("+")
            mm += 1
        li.pop()
        pic.append("-")
        
    if m < b:
        m = b


if flag:
    print("NO")
else:
    for i in pic:
        print(i)
        
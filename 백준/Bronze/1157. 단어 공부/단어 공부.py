import sys

s = sys.stdin.readline().strip()

d = {}

su = s.upper()


for i in range(len(su)):
    if su[i] not in d:
        d[su[i]] = 1
    else:
        d[su[i]] += 1

m = max(d.values())

cnt = 0
ans = 0
for i in d:
    if d[i] == m:
        cnt += 1
        ans = i
        if cnt > 1:
            print("?")
            exit(0)
        
print(ans)
        


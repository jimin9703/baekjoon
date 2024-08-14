import sys

n = int(sys.stdin.readline().strip())

cnt = 0

for i in range(n):
    s = sys.stdin.readline().strip()
    li = []
    for j in range(len(s)):
        if j < len(s) -1:
            if s[j] not in li:
                if s[j] == s[j+1]:
                    pass
                else:
                    li.append(s[j])
            elif s[j] in li:
                break
        else:
            if s[j] not in li:
                pass
                cnt += 1
            elif s[j] in li:
                break

print(cnt)

import sys

dict = {3:'ABC', 4:'DEF', 5:'GHI', 6:'JKL', 7:'MNO', 8:'PQRS', 9:'TUV', 10:'WXYZ'}

s = sys.stdin.readline().strip()

cnt = 0

for i in range(len(s)):
    for j in dict:
        if s[i] in dict[j]:
            cnt += j

print(cnt)

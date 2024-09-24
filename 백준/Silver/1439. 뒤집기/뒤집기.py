import sys

S = list(map(int, sys.stdin.readline().strip()))

a = 0
b = 0

for i in range(len(S)):
    if i == len(S) - 1:
        if S[i] == 1:
            a += 1
        elif S[i] == 0:
            b += 1
    else:
        if S[i] != S[i+1]:
            if S[i] == 1:
                a += 1
            elif S[i] == 0:
                b += 1

print(min(a,b))
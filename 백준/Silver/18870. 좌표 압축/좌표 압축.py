import sys

n = int(sys.stdin.readline().strip())

L = list(map(int, sys.stdin.readline().strip().split()))
D = {}
S = set(L)
S = list(S)
S.sort()

# for i in range(n):
#     for j in range(len(S)):
#         if L[i] == S[j]:
#             L[i] = j

# print(*L)

for i in range(len(S)):
    D[S[i]] = i

for i in range(n):
    L[i] = D[L[i]]

print(*L)

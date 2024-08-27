import sys

b, n = sys.stdin.readline().strip().split()
ans = 0
n = int(n)
b = list(b)
b.reverse()

for i in range(len(b)):
    if b[i].isdigit():
        ans += int(b[i]) * (n ** i)
    elif b[i].isalpha():
        ans += (ord(b[i]) - ord('A') + 10) * (n ** i)

print(ans)
import sys

a, b = map(int, sys.stdin.readline().strip().split())
c = int(sys.stdin.readline().strip())
d = int(sys.stdin.readline().strip())

# if c-a <= 0:
#     print(0)
# else:
#     if d >= b / (c-a):
#         print(1)
#     else:
#         print(0)
if a*d + b <= c*d and c >= a:
    print(1)
else:
    print(0)
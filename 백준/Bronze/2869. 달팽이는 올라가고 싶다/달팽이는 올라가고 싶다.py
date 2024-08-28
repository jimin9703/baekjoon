import sys
import math

a, b, v = map(int, sys.stdin.readline().strip().split())

if (v - a) % (a - b) == 0:
    print((v-a)//(a-b) + 1)
else:
    print(math.ceil((v-a)/(a-b)) + 1)
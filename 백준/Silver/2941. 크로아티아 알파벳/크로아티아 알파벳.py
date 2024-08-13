import sys

s = sys.stdin.readline().strip()

croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alpha in croatian:
    s = s.replace(alpha, "x")
    
print(len(s))
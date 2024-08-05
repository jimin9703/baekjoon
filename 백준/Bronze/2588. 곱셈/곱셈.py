import sys

a = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip()
li_b = [_ for _ in b]



c = a * int(li_b[2])
d = a * int(li_b[1])
e = a * int(li_b[0])
f = a * int(b)

print(c)
print(d)
print(e)
print(f)
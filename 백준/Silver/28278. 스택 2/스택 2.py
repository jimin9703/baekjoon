import sys

input = sys.stdin.readline

n = int(input())


stack = list()

for i in range(n):
    m = list(map(int, input().strip().split()))
    if m[0] == 1:
        stack.append(m[1])
    elif m[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif m[0] == 3:
        print(len(stack))
    elif m[0] == 4:
        if stack:
            print(0)
        else:
            print(1)

    elif m[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
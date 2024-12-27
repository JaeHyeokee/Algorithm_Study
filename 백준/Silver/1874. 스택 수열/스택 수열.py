N = int(input())
stack = []
p = []
k = 1
for i in range(N):
    num = int(input())
    if k <= num:
        while k <= num:
            stack.append(k)
            k += 1
            p.append('+')
        stack.pop()
        p.append('-')
    else:
        p.append('-')
        if stack.pop() != num: break
if len(stack) != 0: print('NO')
else:
    for i in range(len(p)): print(p[i])
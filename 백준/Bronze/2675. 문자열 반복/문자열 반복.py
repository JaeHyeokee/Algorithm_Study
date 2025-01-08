T = int(input())
P = []
for i in range(T):
    R, ch = input().split()
    for j in range(len(ch)): print(ch[j] * int(R), end = '')
    print()
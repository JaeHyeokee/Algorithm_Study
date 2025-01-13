apart = []
for i in range(15):
    if i == 0: apart.append([n + 1 for n in range(14)])
    else:
        tmp = []
        for j in range(14): tmp.append(sum(apart[i - 1][:j + 1]))
        apart.append(tmp)
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(apart[k][n - 1])
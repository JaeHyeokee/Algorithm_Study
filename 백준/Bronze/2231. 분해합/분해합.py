N = int(input())
M = 0
for i in range(1, N):
    tot = i
    tmp = i
    while tmp != 0:
        tot += tmp % 10
        tmp //= 10
    if tot == N:
        M = i
        break
print(M)
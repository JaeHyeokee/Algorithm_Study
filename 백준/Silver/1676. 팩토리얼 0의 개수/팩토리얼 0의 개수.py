def fact(N):
    if N == 0: return 1
    else: return fact(N - 1) * N
def cntZero(N):
    if N % 10 == 0: return cntZero(N // 10) + 1
    else: return 0
num = fact(int(input()))
print(cntZero(num))
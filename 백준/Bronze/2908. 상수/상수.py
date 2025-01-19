def rev(num):
    tmp = 0
    while num != 0:
        tmp *= 10
        tmp += num % 10
        num //= 10
    return tmp
A, B = input().split()
A = rev(int(A))
B = rev(int(B))
if A > B: print(A)
else: print(B)
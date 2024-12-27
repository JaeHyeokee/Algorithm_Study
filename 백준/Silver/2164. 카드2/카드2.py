N = int(input())
i = 0
while N > 2**i: i += 1
print(int((N - 2**(i - 1)) * 2))
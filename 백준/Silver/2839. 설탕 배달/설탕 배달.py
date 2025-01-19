N = int(input())
cnt = 0
if N % 5 == 0: print(N // 5)
else:
    while N > 0:
        N -= 3
        cnt += 1
        if N == 0: break
        elif N < 3:
            cnt = -1
            break
        elif N % 5 == 0:
            cnt += N // 5
            break
    print(cnt)
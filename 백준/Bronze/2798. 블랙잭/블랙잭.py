N, M = map(int, input().split())
arr = list(map(int, input().split()))
tot = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            tmp = arr[i] + arr[j] + arr[k]
            if abs(M - tmp) < abs(M - tot) and tmp <= M: tot = tmp
print(tot)
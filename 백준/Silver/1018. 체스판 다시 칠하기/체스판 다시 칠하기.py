N, M = map(int, input().split())
arr = []
cnt = []
for i in range(N):
    arr.append(input())
for i in range(N - 7):
    for j in range(M - 7):
        start_W = 0
        start_B = 0
        for a in range(8):
            for b in range(8):
                if a % 2 == 0 and b % 2 == 0:
                    if arr[a + i][b + j] == 'W': start_W += 1
                    else: start_B += 1
                elif a % 2 == 0 and b % 2 != 0:
                    if arr[a + i][b + j] == 'B': start_W += 1
                    else: start_B += 1
                elif a % 2 != 0 and b % 2 == 0:
                    if arr[a + i][b + j] == 'B': start_W += 1
                    else: start_B += 1
                else:
                    if arr[a + i][b + j] == 'W': start_W += 1
                    else: start_B += 1
        cnt.append(64 - start_W)
        cnt.append(64 - start_B)
print(min(cnt))
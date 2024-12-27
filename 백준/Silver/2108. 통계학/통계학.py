import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N): arr.append(int(input()))
arr.sort()
cnt = {}
for i in arr:
    if i in cnt: cnt[i] += 1
    else: cnt[i] = 1
max_val = max(cnt.values())
max_arr = []
for i in cnt:
    if cnt[i] == max_val: max_arr.append(i)
S = sum(arr)
if S < 0: print(int(S / N - 0.5))
else: print(int(S / N + 0.5))
print(arr[N // 2])
if len(max_arr) == 1: print(max_arr[0])
else: print(max_arr[1])
print(max(arr) - min(arr))
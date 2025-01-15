def cutTree(arr, start, end, M):
    if end - start <= 1: return start
    mid = (start + end) // 2
    tot = 0
    for i in arr:
        if i - mid > 0: tot += i - mid
    if tot < M: return cutTree(arr, start, mid, M)
    else: return cutTree(arr, mid, end, M)
N, M = map(int, input().split())
arr = list(map(int, input().split()))
print(cutTree(arr, 0, max(arr), M))
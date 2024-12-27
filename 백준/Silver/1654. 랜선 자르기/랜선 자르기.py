def max_length(arr, start, end, N):
    if end - start <= 1: return start
    mid = (start + end) // 2
    cnt = 0
    for i in arr: cnt += i // mid
    if cnt < N: return max_length(arr, start, mid, N)
    else: return max_length(arr, mid, end, N)
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
print(max_length(arr, 0, max(arr) + 1, N))
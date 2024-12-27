def findstr(arr, start, end, num):
    mid = (start + end) // 2
    if arr[mid] == num: return 1
    elif arr[mid] > num:
        if end - start <= 1:
            if arr[start] == num: return 1
            else: return 0
        else: return findstr(arr, start, mid, num)
    else:
        if end - start <= 1:
            if arr[end] == num: return 1
            else: return 0
        else: return findstr(arr, mid, end, num)
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
chk = list(map(int, input().split()))
for i in chk: print(findstr(arr, 0, N - 1, i))
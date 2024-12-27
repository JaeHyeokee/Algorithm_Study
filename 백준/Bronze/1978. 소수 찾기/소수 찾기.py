def isPrimenumber(num):
    if num == 1: return False
    for i in range(2, int(num**(1 / 2)) + 1):
        if num % i == 0: return False
    return True
N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if isPrimenumber(i): cnt += 1
print(cnt)
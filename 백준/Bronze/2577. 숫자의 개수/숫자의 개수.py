num_cnt = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
multi = 1
for i in range(3): multi *= int(input())
while multi != 0:
    num_cnt[multi % 10] += 1
    multi //= 10
for i in num_cnt.values(): print(i)
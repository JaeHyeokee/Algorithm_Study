N = int(input())
series = 666
while True:
    if str(series).find('666') != -1: N -= 1
    if N == 0: break
    series += 1
print(series)
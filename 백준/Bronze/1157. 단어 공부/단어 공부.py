get = input().upper()
cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(get)): cnt[ord(get[i]) - 65] += 1
maxim = cnt[0]
maxin = 0
for i in range(1, 26):
    if maxim < cnt[i]:
        maxim = cnt[i]
        maxin = i
    elif maxim == cnt[i]: maxin = -2
print(chr(maxin + 65))
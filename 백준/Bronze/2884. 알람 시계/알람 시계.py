H, M = input().split()
sec = int(H) * 60 + int(M) - 45
if sec < 0: sec = 24 * 60 + sec
print(sec // 60, sec % 60)
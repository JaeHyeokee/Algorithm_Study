get = input().split()
idn = 0
for i in range(len(get)): idn += int(get[i])**2
print(idn % 10)
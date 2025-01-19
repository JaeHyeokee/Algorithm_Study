get = input().split()
music = ''
for i in range(len(get)): music += get[i]
if music == '12345678': print('ascending')
elif music == '87654321': print('descending')
else: print('mixed')
for i in range(int(input())):
    order = input()
    size = int(input())
    get = input()
    if get == '[]': arr = []
    else: arr = list(map(int, get[1:len(get) - 1].split(',')))
    comp = True
    rev = 0
    for j in range(len(order)):
        if order[j] == 'R': rev = abs(rev - 1)
        else:
            if len(arr) == 0:
                comp = False
                break
            if rev == 0: arr.pop(0)
            else: arr.pop(-1)
    if comp == False: print('error')
    else:
        if rev == 1: arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']')
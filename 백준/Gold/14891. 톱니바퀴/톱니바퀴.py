cog = []
con = [True, True, True]
turn = [0, 0, 0, 0]
tot = 0

def checkCon(cog, con):
    for i in range(3):
        if cog[i][2] == cog[i + 1][6]: con[i] = False
        else: con[i] = True

def setTurn(con, turn, num, dir):
    turn[num - 1] = dir
    for i in range(num - 1, 0, -1):
        if con[i - 1] == True: turn [i - 1] = -turn[i]
        else: turn[i - 1] = 0
    for i in range(num - 1, 3):
        if con[i] == True: turn [i + 1] = -turn[i]
        else: turn[i + 1] = 0

for i in range(4):
    tmp = input()
    tmp2 = []
    for j in range(len(tmp)): tmp2.append(int(tmp[j]))
    cog.append(tmp2)

for i in range(int(input())):
    num, dir = map(int, input().split())
    checkCon(cog, con)
    setTurn(con, turn, num, dir)
    for j in range(4):
        if turn[j] == 1: cog[j].insert(0, cog[j].pop())
        elif turn[j] == -1: cog[j].append(cog[j].pop(0))

for i in range(4):
    if cog[i][0] == 1: tot += 2 ** i
print(tot)
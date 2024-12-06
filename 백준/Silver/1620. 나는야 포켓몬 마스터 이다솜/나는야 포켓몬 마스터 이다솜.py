import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pocket_mon = dict()
for i in range(N):
    temp = input().strip()
    pocket_mon[temp] = i + 1
    pocket_mon[i + 1] = temp
for i in range(M):
    quiz = input().strip()
    if quiz.isdigit(): print(pocket_mon[int(quiz)])
    else: print(pocket_mon[quiz])
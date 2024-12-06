N = int(input())
score = input().split()
for i in range(N): score[i] = int(score[i])
M = max(score)
for i in range(N): score[i] = score[i] / M * 100
print(sum(score) / N)
import sys
input = sys.stdin.readline
arr = []
for i in range(int(input())): arr.append(int(input()))
for i in sorted(arr): print(i)
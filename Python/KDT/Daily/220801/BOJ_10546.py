import sys

input = sys.stdin.readline

n = int(input())
runner = {}

for i in range(n):
    p = input()
    
    if p in runner:
        runner[p] += 1
    else:
        runner[p] = 1

for i in range(n-1):
    p = input()
    runner[p] -= 1

for i in runner:
    if runner[i] == 1:
        print(i)
        break
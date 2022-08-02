import sys

input = sys.stdin.readline

n, m = map(int, input().split())

x = []
for _ in range(n):
    elem = input()
    x.append(elem)

y = []
cnt = 0
for _ in range(m):
    elem = input()
    if elem in x:
        cnt += 1
print(cnt)
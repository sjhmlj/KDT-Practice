import sys
input = sys.stdin.readline

chess = [list(input()) for _ in range(8)]
cnt = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0 and chess[i][j] == 'F':
                cnt += 1
        elif i % 2 == 1:
            if j % 2 == 1 and chess[i][j] == 'F':
                cnt += 1

print(cnt)
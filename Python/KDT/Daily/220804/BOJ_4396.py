import sys

input = sys.stdin.readline

# input
N = int(input())
mine = [list(input().rstrip()) for _ in range(N)]
play = [list(input().rstrip()) for _ in range(N)]
ans = [['.' for _ in range(N)] for _ in range(N)]
# 방향 벡터 
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]

flag = False

for i in range(N):
    cnt = 0
    for j in range(N):
        if play[i][j] == 'x':
            cnt = 0
            
            if mine[i][j] == '*':
                flag = True
            
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]

                if 0 <= x < N and 0 <= y < N:
                    if mine[x][y] == '*':
                        cnt += 1
            ans[i][j] = str(cnt)
if flag:
    for i in range(N):
        for j in range(N):
            if mine[i][j] == '*':
                ans[i][j] = '*'

for i in range(N):
    print(''.join(ans[i]))

        
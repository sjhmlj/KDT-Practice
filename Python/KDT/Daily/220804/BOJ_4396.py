'''
Q. 지뢰 찾기
- 상하좌우, 대각선으로 인접한 8개의 칸에 대한 알림
- 즉 시계방향(또는 반시계)로 탐색을 진행
'''
import sys


input = sys.stdin.readline

n = int(input())
# . : 지뢰 없음 / * : 지뢰
grid = [list(input().rstrip()) for _ in range(n)]
# x : 열림 / . : 열리지 않음
game = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]

ans = [['.' for _ in range(n)] for _ in range(n)]
flag = False

for i in range(n):
    for j in range(n):
        if game[i][j] == 'x':
            cnt = 0

            if grid[i][j] == '*':
                flag = True
            
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]

                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == '*':
                        cnt += 1
            ans[i][j] = str(cnt)

if flag:
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                ans[i][j] = '*'

for i in range(n):
    print(''.join(ans[i]))
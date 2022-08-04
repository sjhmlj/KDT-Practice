''''
Q. 누울 자리를 찾아라
- N 정사각형 방
- 빈 칸 연속 2칸 이상이면 누울 자리 
- 가로로, 세로로 눕는 경우 2가지
- 누우면 벽 또는 짐에 닿는다 (짐 제외 꽉 차지함)
'''

import sys

input = sys.stdin.readline

N = int(input())
case = [list(input().rstrip()) for _ in range(N)]

row_cnt = 0
col_cnt = 0

for i in range(N):
    check = 0

    for j in range(N):
        # '.' 를 만나는 경우 
        if case[i][j] == '.':
            check += 1
        # 'X'를 만나는 경우 => 여기까지 누울 수 있는지 확인
        else:
            if check >= 2:
                row_cnt += 1
                check = 0
            else:
                check = 0
    # 'X'를 만나지 않았으나 '.' 2개 이상인 경우 (마지막 경우의 수 체크)
    if check >= 2:
        row_cnt += 1

# transpose 구현
new_case = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        new_case[i][j] = case[j][i]

for i in range(N):
    check = 0

    for j in range(N):
        if new_case[i][j] == '.':
            check += 1
        else:
            if check >= 2:
                col_cnt += 1
                check = 0
            else:
                check = 0
    if check >= 2:
        col_cnt += 1

print(row_cnt, col_cnt)       
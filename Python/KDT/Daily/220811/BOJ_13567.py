'''
Q. 로봇 
TURN + 0 => 왼쪽 90도 회전, + 1 => 오른쪽 90도 회전
MOVE + N => N만큼 직진
명령 수행 후 범위 내에 있으면 명령 유효
바깥으로 나가게 되면 명령어 유효 x 
결국 바깥에 있는 경우 -1 출력
'''
### 미완료

import sys

sys.stdin = open('input_13567.txt', 'r')
# M : 정사각형 한 변의 길이, 오른쪽 맨 끝(M, M)
M, n = map(int, input().split())

field = [[0 for _ in range(M)] for _ in range(M)]

for _ in range(n):
    act, num = input().split()

    if act == 'MOVE':
        if 

    elif act == 'TURN':
        if num == 0:

        elif num == 1:
'''
* 문제 : 가위바위보 판정
* 접근
    * 가위(1), 바위(2), 보(3) / no draw
    * 숫자가 크면 이긴다
    * 단, 가위와 보의 관계는 반대
    * 이긴 사람 출력
'''

import sys

sys.stdin = open('input_1936.txt', 'r')

a, b = map(int, input().split())

if (a > b) or (a == 1):
    winner = 'A'
else:
    winner = 'B'

print(winner)

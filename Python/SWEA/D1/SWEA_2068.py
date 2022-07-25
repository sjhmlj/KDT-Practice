'''
* 문제 : 최대수 구하기
* 접근
    * list 객체 max() 활용
'''

import sys

sys.stdin = open('input_2068.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    case = list(map(int, input().split()))
    print('#{} {}'.format(i, max(case)))
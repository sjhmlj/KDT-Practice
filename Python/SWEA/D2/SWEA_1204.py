'''
* 문제 : 최빈수 구하기
* 접근
    * 최빈수 : 가장 많이 나타난 값
    * 순회하며 요소에 대한 count로 값 비교
'''

import sys

sys.stdin = open('input_1204.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    num = int(input())
    case = list(map(int, input().split()))
    
    max_cnt = 0
    for score in case:
        cnt = case.count(score)
        if max_cnt < cnt:
            max_cnt = cnt
            result = score
    
    print('#{} {}'.format(i, result))
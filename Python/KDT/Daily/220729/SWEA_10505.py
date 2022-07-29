'''
* 문제 : 소득 불균형
n명의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람 수 출력

* input
1) test case T
2) numbers of people N and 평균 소득case

* output
1) 평균 이하의 소득을 가진 사람 수
'''

import sys

sys.stdin = open('input_10505.txt', 'r')

# input 1) test case
T = int(input())

# input 2) 사람수 N에 대한 각 case
for i in range(1, T + 1):
    N = int(input())
    case = list(map(int, input().split()))
    
    avg = sum(case) // N
    cnt = 0

    for person in case:
        if person <= avg:
            cnt += 1

    print('#{} {}'.format(i, cnt))
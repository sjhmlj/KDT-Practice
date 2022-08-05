'''
1. input
* 수강생 n명
* 과제 제출한 사람의 목록

2. output
* 과제를 제출하지 않은 사람의 목록
'''

import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for tc in range(1, T + 1):
    # n : 수강생, k : 제출자 수
    n, k = map(int, input().split())

    # case : 제출한 사람 출석 명단
    case = list(map(int, input().split()))

    print('#{}'.format(tc), end=' ')
    for i in range(1, n + 1):
        if i not in case:
            print(i, end=' ')
    print()

'''
* 문제 : 홀수만 더하기
* 접근
    * for loop로 각 요소 홀수 확인하여 합
'''

import sys

sys.stdin = open('input_2072.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    case = list(map(int, input().split()))
    ans = 0

    for num in case:
        if num % 2 == 1:
            ans += num
    
    print('#{} {}'.format(i, ans))
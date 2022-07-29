'''
* 문제 : 신용카드 만들기 2
- 신용카드 조건
1) 카드 번호 시작 : 3, 4, 5, 6, 9
2) '-' 들어갈 수 있으며 '-'를 제외한 숫자는 16개

주어진 번호가 신용카드가 될 수 있는지 판별하시오

* input
1) test case T
2) str case

* output
1) 1/0 으로 판별
'''

import sys

sys.stdin = open('input_14654.txt', 'r')

# input 1) test case
T = int(input())
num_first = '34569'

for i in range(1, T + 1):
    case = ''.join(input().split('-'))

    if (case[0] not in num_first) or len(case) != 16:
        result = 0
    else:
        result = 1
    
    print('#{} {}'.format(i, result))
'''
* 문제 : n, 2n, 3n, 4n, 5n 으로 카운팅 / 0~9 모두 나오면 종료
* 접근
    * k배로 증가
    * 0~9를 모두 목격해야함 => list로 처리
    * while loop
'''

import sys

sys.stdin = open('input_1288.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    number = int(input())
    case = []
    k = 1
    cnt = 0

    while True:
        num = str(number * k)
        for digit in num:
            case.append(digit)  
        case = list(set(case))  # 중복 제거

        if len(case) == 10:
            cnt += 1
            break
        k += 1
        cnt += 1

    print('#{} {}'.format(i, cnt * number))

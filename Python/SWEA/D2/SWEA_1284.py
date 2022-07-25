'''
* 문제 : 수도값 계산하여 비교
* 접근
    * 조건에 따른 수식 정의하여 비교
'''

import sys

sys.stdin = open('input_1284.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    price_a = p * w
    price_b = q if w <= r else ((w-r) * s) + q
    payment = min(price_a, price_b)

    print('#{} {}'.format(i, payment))
'''
* 문제 : 몫과 나머지 출력
* 접근
  * 산술연산자 활용
'''

import sys

sys.stdin = open('input_2029.txt', 'r')

T = int(input())

for i in range(1, T + 1):
  a, b = map(int, input().split())
  print('#{} {} {}'.format(i, a // b, a % b))

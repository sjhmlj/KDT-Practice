'''
* 문제 : 크기 비교하여 부등호 출력
* 접근
  * 비교연산자 활용
'''

import sys

sys.stdin = open('input_2070.txt', 'r')

T = int(input())

for i in range(1, T + 1):
  a, b = map(int, input().split())

  if a > b:
    result = '>'
  elif a < b:
    result = '<'
  else:
    result = '='
  
  print('#{} {}'.format(i, result))
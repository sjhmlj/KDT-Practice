'''
* 문제 : 평균값 구하기
* 접근
  * avg = sum() / len()
'''

import sys

sys.stdin = open('input_2071.txt', 'r')

T = int(input())

for i in range(1, T + 1):
  case = list(map(int, input().split()))
  avg = sum(case) / len(case)
  
  print('#{} {:.0f}'.format(i, avg))
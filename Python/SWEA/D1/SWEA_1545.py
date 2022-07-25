'''
* 문제 : 거꾸로 출력
* 접근
  * for loop
'''

import sys

sys.stdin = open('input_1545.txt', 'r')

n = int(input())

for i in range(n, -1, -1):
  print(i, end=' ')

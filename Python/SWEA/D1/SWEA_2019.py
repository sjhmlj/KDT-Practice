'''
* 문제 : 순회하며 2의 제곱 출력
* 접근
  * for loop 를 통해 순회
  * 2의 제곱에 대한 i
'''

import sys

sys.stdin = open('input_2019.txt', 'r')

n = int(input())

for i in range(n + 1):
  print(2 ** i, end=' ')
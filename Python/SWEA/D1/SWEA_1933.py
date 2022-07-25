'''
* 문제 : n의 약수
* 접근
  * 순회하며 특정 조건을 만족할 경우 출력
'''

import sys

sys.stdin = open('input_1933.txt', 'r')

n = int(input())

for i in range(1, n + 1):
  if n % i == 0:
    print(i, end=' ')
'''
* 문제 : 알파벳을 숫자로 표현
* 접근
  * ASCII code 활용
  * for loop
'''

import sys

sys.stdin = open('input_2050.txt', 'r')

s = input()

for word in s:
  print(ord(word) - 64, end=' ')

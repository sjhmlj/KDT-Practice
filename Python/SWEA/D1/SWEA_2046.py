'''
* 문제 : 정해진 숫자만큼 스탬프 찍기
* 접근
  * 문자열 곱
'''

import sys

sys.stdin = open('input_2046.txt', 'r')

n = int(input())

print('#' * n)
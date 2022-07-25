'''
* 문제 : 사칙연산에 대한 간단한 입출력
* 접근
    * 산술연산자 및 print() 활용
'''

import sys

sys.stdin = open('input_1938.txt', 'r')

a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
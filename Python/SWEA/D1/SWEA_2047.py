'''
* 문제 : 주어진 문자열 전부 대문자로 표현
* 접근
     * .upper() method
     * ASCII code활용도 가능
'''

import sys

sys.stdin = open('input_2047.txt', 'r')

title = input().upper()

print(title)
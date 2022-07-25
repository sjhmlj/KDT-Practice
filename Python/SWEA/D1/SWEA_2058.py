'''
* 문제 : 자릿수별로 더하기
* 접근
    * 1 <= n <= 9999 => 자릿수가 정해져 수치로 접근 가능
    * 순회하며 문자열 접근이 더 좋을듯
'''

import sys

sys.stdin = open('input_2058.txt', 'r')

num = input()
ans = 0

for digit in num:
    ans += int(digit)

print(ans)
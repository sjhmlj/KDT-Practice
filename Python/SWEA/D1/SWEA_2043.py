'''
* 문제 : 비밀번호 맞추기
* 접근
  * k 부터 1씩 증가하며 비밀번호 p와 대조
  * 같아지는데까지 카운트 (마지막 숫자가 비밀번호이니 조건문 없이 카운트)
'''

import sys

sys.stdin = open('input_2043.txt', 'r')

p, k = map(int, input().split())
cnt = 0

for i in range(k, p + 1):
  cnt += 1

print(cnt)
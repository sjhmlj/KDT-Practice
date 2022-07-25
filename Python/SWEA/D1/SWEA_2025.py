'''
* 문제 : 1부터 n 까지의 합
* 접근
  * for loop
'''

import sys

sys.stdin = open('input_2025.txt', 'r')

n = int(input())
ans = 0

for i in range(1, n + 1):
  ans += i

print(ans)
'''
* 문제 : 연월일 구분하여 출력
* 접근
  * slicing으로 연월일 구분
  * 월에 따른 일수 확인
'''

import sys

sys.stdin = open('input_2056.txt', 'r')

T = int(input())

for i in range(1, T + 1):
  case = input()
  year = case[:4]
  month = case[4:6]
  day = case[6:]

  if (int(month) in [1, 3, 5, 7, 8, 10, 12]) and (1 <= int(day) <= 31):
    print('#{} {}/{}/{}'.format(i, year, month, day))
  elif (int(month) in [4, 6, 9, 11]) and (1 <= int(day) <= 30):
    print('#{} {}/{}/{}'.format(i, year, month, day))
  elif (int(month) == 2) and (1 <= int(day) <= 28):
    print('#{} {}/{}/{}'.format(i, year, month, day))
  else:
    print('#{} {}'.format(i, -1))

  
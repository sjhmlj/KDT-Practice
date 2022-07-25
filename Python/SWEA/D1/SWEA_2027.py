'''
* 문제 : 대각선 출력
* 접근
  * 이중 for loop 중 i == j 에서 대각선 표시
'''

for i in range(5):
  for j in range(5):
    if i == j:
      shape = '#'
    else:
      shape = '+'
    print(shape, end='')
  print()
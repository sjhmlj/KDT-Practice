'''
* 문제 : 계단 모양의 별찍기(2)
* 접근
    * 특정 횟수의 별찍기, 줄바꾸기의 위치를 고려한 for loop
'''

n = int(input())

for i in range(n):
    for j in range(n - 1 - i):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()
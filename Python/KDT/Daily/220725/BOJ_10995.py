'''
* 문제 : 별찍기
* 접근
    * 조건에 따른 반복문 작성
'''

n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print(' *' * n)
    else:
        print('* ' * n)

        
        
'''
* 문제 : 구구단 출력
* 접근
    * 출력양식을 맞춰 for loop
'''

n = int(input())

for i in range(1, 10):
    print('{} * {} = {}'.format(n, i, n * i))
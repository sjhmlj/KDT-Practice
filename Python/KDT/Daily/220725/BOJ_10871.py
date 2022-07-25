'''
* 문제 : x보다 작은 수
* 접근
    * list에 대하여 특정 조건에 대한 색출, for loop로 접근 
'''

n, x = map(int, input().split())
case = list(map(int, input().split()))

for num in case:
    if num < x:
        print(num, end=' ')
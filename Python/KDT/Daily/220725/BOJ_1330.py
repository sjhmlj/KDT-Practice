'''
* 문제 : 두 수 비교하여 부등호 출력
* 접근
    * 비교연산자 활용한 두 수의 크기 비교
'''

a, b = map(int, input().split())

if a > b: result = '>'
elif a < b: result = '<'
else: result = '=='

print(result)
'''
* 문제 : 간단한 출력
* 접근
    * 합 출력
'''

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(a + b)
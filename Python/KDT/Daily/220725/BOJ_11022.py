'''
* 문제 : 간단한 입출력
* 접근
    * 합 출력
''' 

T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())

    print('Case #{}: {} + {} = {}'.format(i, a, b, a + b))
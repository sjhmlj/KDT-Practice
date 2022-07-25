'''
* 문제 : 간단한 출력
* 접근
    * 합 출력
    * 특정 조건에서 반복문 종료 => while loop
'''

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    
    print(a + b)
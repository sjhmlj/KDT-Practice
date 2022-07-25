'''
* 문제 : 한수의 개수 출력
* 접근
    * 정의 : 각 자리가 등차수열 => 한수
    * 1 <= n <= 1000
        * 두자리수는 무조건 한수
        * 세자리수에 대해서 조건문
'''

# 한수의 개수를 출력하는 함수 정의
def hansoo(n):
    cnt = 0

    # 1부터 n(포함)까지 순회하여 조건에 따라 카운팅
    for num in range(1, n + 1):
        if num < 100:
            cnt += 1
        # 각 자릿수의 차가 같은 경우 == 등차수열 => 한수
        elif (num // 100 - num % 100 // 10) == (num % 100 // 10 - num % 10):
            cnt += 1
        
    return cnt

n = int(input())

print(hansoo(n))


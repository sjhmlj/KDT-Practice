'''
* 문제 : n이 주어졌을 때 n의 가장 작은 생성자 찾기
* 접근
    * 분해합 함수 정의
        * return value == 생성자
    * 순회하며 생성자가 나올 때까지 반복
        * break문에 걸리지 않고 끝나는 경우 0 출력
'''
# 분해합 입력
n = int(input())

# n : 생성자, sum_val : 분해합
def func1(n):
    sum_val = n
    for i in str(n):
        sum_val += int(i)

    return sum_val    

# 생성자 i를 통해 만들어지는 함수 결과가 입력한 분해합과 같은 순간 출력
for i in range(1, n + 1):
    if func1(i) == n:
        print(i)
        break
else:
    print(0)
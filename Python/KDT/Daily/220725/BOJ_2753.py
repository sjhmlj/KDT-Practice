'''
* 문제 : 윤년
* 접근
    * 일정 조건을 만족하는 윤년 출력 (1 / 0)
'''

year = int(input())
result = 0

if (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0:
    result = 1

print(result)
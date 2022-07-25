'''
* 문제 : list의 최대 최소
* 접근
    * 리스트에 대한 최대 최소 함수 적용
'''

n = int(input())
case = list(map(int, input().split()))

print(min(case), max(case))
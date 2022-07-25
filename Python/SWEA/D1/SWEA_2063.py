'''
* 문제 : 중간값 찾기
* 접근
    * list 요소 개수는 홀수
    * 오름차순 정렬 후 가운데 idx접근
'''

import sys

sys.stdin = open('input_2063.txt', 'r')

n = int(input())
case = list(map(int, input().split()))

case.sort()

print(case[n // 2])
'''
* 문제 : 최빈수 구하기
1000명의 수학성적으로 통계자료 제작
최빈수를 활용하여 평균 수준 짐작
- 최빈수 : 가장 여러 번 나타난 값

* input
1) test case  : T
2) test case number (n), 1000명의 점수

* output
1) 주어진 양식과 함께 최빈수
'''

import sys

sys.stdin = open('input_1204.txt', 'r')

# input 1) test case
T = int(input())

# input 2) test number(n) and 1000명의 점수(case)
for i in range(1, T + 1):
    n = int(input())
    case = list(map(int, input().split()))
    static = {}

    for score in case:
        if score in static:
            static[score] += 1
        else:
            static[score] = 1
    
    max_count = 0

    for score in static:
        if static[score] > max_count:
            max_count = static[score]
            max_count_score = score
    
    print('#{} {}'.format(i, max_count_score))
            
    
    
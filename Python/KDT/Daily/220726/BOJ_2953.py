'''
* 문제 : 평가 점수를 기반으로 우승자와 그 점수 구하기
* 접근
    * 1~5점 / 다섯명의 참가자 (4명의 점수)
    * 합산 결과를 list로 정의, list comprehension 활용
'''
case = [sum(list(map(int, input().split()))) for i in range(5)]
print(case.index(max(case)) + 1, max(case))
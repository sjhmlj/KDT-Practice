'''
* 문제 : 조건에 따른 시험 성적
* 접근
    * 점수 범위에 대한 분기
    * elif를 통해 이전의 조건에 대한 filtering
'''

score = int(input())

if 90 <= score <= 100:
    result = 'A'
elif 80 <= score:
    result = 'B'
elif 70 <= score:
    result = 'C'
elif 60 <= score:
    result = 'D'
else:
    result = 'F'

print(result)
'''
1. input
* 총점 = 중간 35 + 기말 45 + 과제 20
* 학점은 같은 동일한 비율로 할당
'''

import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for tc in range(1, T + 1):
    # n : 전체 학생 수, k : 학점 확인 요청자 번호
    n, k = map(int, input().split())
    # score[i][0] : 중간 / score[i][1] : 기말 / score[i][2] : 과제
    score = [list(map(int, input().split())) for _ in range(n)]
    total = []

    # algorithm 1. 총점 계산하여 내림차순 정렬
    for i in range(n):
        # k번째 학생의 점수 따로 저장
        if i == k - 1:
            k_score = 0.35 * score[i][0] + 0.45 * score[i][1] + 0.2 * score[i][2]
        total.append(0.35 * score[i][0] + 0.45 * score[i][1] + 0.2 * score[i][2])

    result = sorted(total, reverse=True)

    grade = [
            'A+', 'A0', 'A-',
            'B+', 'B0', 'B-',
            'C+', 'C0', 'C-',
            'D0'
            ]
    
    # algorithm 2. k_socre에 따른 학점 부여
    person_per_grade = n // 10  # 학점당 부여 가능한 사람 수

    cnt = 0
    for i in range(0, len(result), person_per_grade):
        if k_score in result[i : i + person_per_grade]:
            k_grade = grade[cnt]
            break
        cnt += 1

    print('#{} {}'.format(tc, k_grade))

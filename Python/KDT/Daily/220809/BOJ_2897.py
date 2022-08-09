'''
Q. 몬스터 트럭
- 지도 : R행 C열 table
- 빌딩 (#), 주차된 차 (X), 빈 공간 (.) 표시
- 해빈이 트럭 -> 2행 2열 칸 차지
- 주차하기 위해 부숴야만 하는 차의 수는?
* 빌딩 부술 수 없음, 가는 길에 부수는 차 허용

* output
line 1 : 아무 차도 부수지 않고 주차 가능한 공간의 수
line 2 : 한 대만 부수고 주차할 수 있는 공간의 수
'''
# input 
R, C = map(int, input().split())
case = [list(input()) for _ in range(R)]
'''
#..#
..X.
..X.
#XX#
'''

# 시계방향 벡터
dr = [0, 0, 1, 1]
dc = [0, 1, 1, 0]

# 결과 result 초기화 (문제 조건에 따름)
result = [0 for _ in range(5)]

for i in range(R):
    for j in range(C):
        # 특정 지점 값 point 변수에 저장
        point = case[i][j]

        # 건물이 아닌 경우 통과하여 진행
        if point != '#':
            car = 0
            cnt = 0
            # 현재 지점 포함 시계방향으로 4칸 캄색
            for k in range(4):
                r = i + dr[k]
                c = j + dc[k]

                # 범위를 벗어나지 않는 중
                if 0 <= r < R and 0 <= c < C:
                    # 건물을 만나는 경우 반복문 탈출
                    if case[r][c] == '#':
                        break
                    # 차를 만나는 경우
                    elif case[r][c] == 'X':
                        car += 1
                        cnt += 1
                    # 빈 공간일 경우
                    else:
                        cnt += 1
            # 탐색 완료 후 4칸 정상 진행한 경우
            if cnt == 4:
                result[car] += 1

for i in result:
    print(i)


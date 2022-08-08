'''
Q. 오목
- 19x19
- 5개 연속 => 승리
- 가로, 세로, 대각선 방향 모두 가능
- 여섯알 이상이 연속적으로 놓인 경우 승리 X

승부 판단 프로그램 (1 / 2/ 0)
'''
import sys

case = [list(map(int, input().split())) for _ in range(19)]
game = False

# 우상 / 우 / 우하 / 하에 대한 벡터
dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

for i in range(19):
    for j in range(19):
        if case[i][j]:
            # 반복문에서 비교를 위해 초기값 저장
            target = case[i][j]

            for k in range(4):
                cnt = 1
                # 우상 -> 우 -> 우하 -> 하 순서로 탐색
                r = i + dr[k]
                c = j + dc[k]

                while (0 <= r < 19) and (0 <= c < 19) and (case[r][c] == target):
                    cnt += 1

                    # 오목 만족시 육목 체크
                    if cnt == 5:
                        # 육목 case 1 : 초기값 전 단계 == 초기값 (=> 6목)
                        if 0 <= i - dr[k] < 19 and 0 <= j - dc[k] < 19 and case[i-dr[k]][j-dc[k]] == target:
                            break

                        # 육목 case 2 : 마지막 다음 단계 == 초기값 (=> 6목)
                        elif 0 <= r + dr[k] < 19 and 0 <= c + dc[k] < 19 and case[r+dr[k]][c+dc[k]] == target:
                            break

                        # 오목 만족일 경우
                        print(target)  # 초기값 == 승리시 돌
                        print(i + 1, j + 1)  # 돌의 초기 좌표 +1 == 실제 바둑판에서의 위치
                        sys.exit(0)  # 프로그램 종료

                    # 진행중이던 방향 유지하여 탐색
                    r += dr[k]
                    c += dc[k]

# 판정을 했는데 정상 종료가 되지 않는 경우 => 무승부
print(0)
import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for tc in range(1, T + 1):
    # n : 파리 배열, m : 파리채 배열
    n, m = map(int, input().split())

    # 파리 전체 분포
    case = [list(map(int, input().split())) for _ in range(n)]

    max_catch = 0

    for i in range(n):
        for j in range(n):
            catch = 0
            # 파리 2차원 배열에 대하여 파리채 배열 크기만큼의 요소들을 더해감
            for x in range(j, j + m):
                # x의 값이 파리채 범위를 넘어가는 경우 break
                if x > n - 1:
                    break
                for y in range(i, i + m):
                    if y > n - 1:
                        break
                    catch += case[y][x]
            # max 값 최신화
            if max_catch < catch:
                max_catch = catch

    print('#{} {}'.format(tc, max_catch))        



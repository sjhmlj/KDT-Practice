'''
Q. 섬의 개수
- 1 : 땅 / 0 : 바다
- 가로, 세로, 대각선으로 연결되어있으면 걸어갈 수 있음
'''
import sys

sys.setrecursionlimit(10000)
sys.stdin = open('input_4963.txt', 'r')

def dfs(r, c):
    # 섬으로 확인된 구역은 0으로 만들어서 방문 처리
    map_[r][c] = 0

    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        # 탐색에 따른 다음 좌표의 결과가 주어진 필드를 벗어나지 않고 섬인 경우 이어서 탐색
        if 0 <= nr < h and 0 <= nc < w and map_[nr][nc] == 1:
            dfs(nr, nc)

# 8방위 시계방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    # 지도 전체 면적
    w, h = map(int, input().split())
    
    # 입력 종료 조건
    if w == 0 and h == 0:
        break
    
    # 지도 초기화 및 섬 개수 cnt 초기화
    map_ = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            # 해당 좌표의 요소가 1(섬)인 경우 dfs탐색, 탐색할 때 마다 cnt += 1 진행
            if map_[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    print(cnt)
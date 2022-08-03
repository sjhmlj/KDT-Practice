import sys

input = sys.stdin.readline

# 참가자 수
n = int(input())

card = [list(map(int, input().split())) for _ in range(n)]

score = [0 for _ in range(n)]

for i in range(3):
    target = []
    # 열을 구분하여 묶은 target 리스트를 먼저 생성
    for j in range(n):
        target.append(card[j][i])
    
    # target에 하나만 있는 경우 그 점수만큼 추가 (j는 플레이어 넘버와도 일치)
    for j in range(n):
        if target.count(card[j][i]) == 1:
            score[j] += card[j][i]
    
for i in score:
    print(i)

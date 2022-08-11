'''
Q. 킹
- 킹의 위치가 주어짐
- 알파벳(A~H) : 열, 숫자(1~8) : 행
- 명령어로 동작
    R / L / B / T 
    RT / LT / RB / LB
'''
import sys

sys.stdin = open('input_1063.txt', 'r')

# 명령어에 따른 탐색 방향
cmds = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dr = [0, 0, 1, -1, -1, -1, 1, 1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]

king_position, stone_position, move = input().split()

# 받은 입력값 조건에 맞게 환산
# 열(문자) => 아스키코드 활용하여 수치화
# 행(숫자) => 행의 위아래가 바뀌도록 수식 활용
king_r = 8 - int(king_position[1])
king_c = ord(king_position[0]) - 65

stone_r = 8 - int(stone_position[1])
stone_c = ord(stone_position[0]) - 65


for _ in range(int(move)):
    cmd = input()
    # 받은 명령어의 index값을 통해 탐색 방향 참조
    for i in range(len(cmds)):
        if cmds[i] == cmd:
            k = i

    king_nr = king_r + dr[k]
    king_nc = king_c + dc[k] 
    
    # 킹의 다음 좌표가 체스판을 벗어나는 경우 전개하지 않고 다음 명령어 받음
    if king_nr > 7 or king_nr < 0 or king_nc > 7 or king_nc < 0:
        continue
    
    # 킹의 다음 좌표에 돌이 있는 경우
    # 우선 돌을 왕이 움직이는 만큼 움직인 후 체스판을 벗어났는지 확인
    if king_nr == stone_r and king_nc == stone_c:
        stone_nr = stone_r + dr[k]
        stone_nc = stone_c + dc[k]
        # 벗어난 경우 돌은 움직이지 않음
        if stone_nr > 7 or stone_nr < 0 or stone_nc > 7 or stone_nc < 0:
            continue 
        
        stone_r = stone_nr
        stone_c = stone_nc
    
    king_r = king_nr
    king_c = king_nc

# 최종 좌표에 대한 환산 (원래대로 돌림)
king_position = chr(king_c + 65) + str(8 - king_r)
stone_position = chr(stone_c + 65)+ str(8 - stone_r)

print(king_position)
print(stone_position)

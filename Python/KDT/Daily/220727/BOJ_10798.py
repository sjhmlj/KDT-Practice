'''
세로 읽기
'''

board = []
width = []
for i in range(5):
    text = list(input())
    board.append(text)
    width.append(len(text))

for x in range(max(width)):
    for y in range(5):
        if len(board[y]) > x:
            print(board[y][x], end='')
        else:
            continue
        

'''
* 카드게임
0~9까지 일렬로 깔아놓음 
10라운드, 이김 (+3) 비김 (+1) 
총 승점 비교, 같은 경우 마지막에 이긴 사람이 승자
모든 라운드에서 비긴 경우 <최종 무승부> 
'''

a = list(map(int, input().split()))
b = list(map(int, input().split()))

win = []

for i in range(10):
    if a[i] > b[i]:
        win.append('A')
    elif a[i] < b[i]:
        win.append('B')
    else:
        win.append('D')

a_point = 3 * win.count('A') + win.count('D')
b_point = 3 * win.count('B') + win.count('D')

if a_point > b_point:
    winner = 'A'
elif a_point < b_point:
    winner = 'B'
else:
    for i in range(len(win) - 1, -1, -1):
        if win[i] != 'D':
            winner = win[i]
            break
        else:
            winner = 'D'    

print(a_point, b_point)
print(winner)

'''
Q. 직사각형 네개의 합집합의 면적 구하기
- 합집합의 넓이의 합
- 격자 하나의 넓이 == 1
'''

grid = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(lambda x : int(x) - 1, input().split())
    ans = 0
    # 해당 좌표에 1 표시
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = 1
    
    for i in range(100):
        for j in range(100):
            ans += grid[i][j]

print(ans) 

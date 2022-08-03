# 느려터져서 PyPy3로 실행

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
case = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

sum_ = [0 for _ in range(k)]

for order in range(k):
    i, j, x, y = map(lambda x : int(x) - 1, input().split())
    
    # 좌표가 같을 때 
    if i == x and j == y:
        sum_[order] = case[i][j]
        continue
    for r in range(i, x + 1):
        for c in range(j, y + 1):
            sum_[order] += case[r][c]

for i in sum_:
    print(i)




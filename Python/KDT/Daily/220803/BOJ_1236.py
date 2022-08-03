'''
맞왜틀???
=> 열 탐색 때 인덱싱을 잘못했었다...! 
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
case = [list(input().rstrip()) for _ in range(n)]
row = 0
col = 0

#행 탐색
for i in range(n):
    if 'X' not in case[i]:
        row += 1
#열 탐색
for j in range(m):
    col_list = []
    for i in range(n):
        col_list.append(case[i][j])
    
    if 'X' not in col_list:
        col += 1

print(max(row, col))

# output은 일치하지만 시간초과 알고리즘
# for i in range(n):
#     if 'X' not in case[i]:
#         for j in range(m):
#             if 'X' == case[i][j]:
#                 break
#         else:
#             cnt += 1
# print(cnt)
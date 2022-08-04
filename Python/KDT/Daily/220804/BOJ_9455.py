'''
Q. 박스

'''

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())

    case = [list(map(int, input().split())) for _ in range(m)]

    # 전치 행렬 new_case
    new_case = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):  # 5
        for j in range(n):  # 4
            new_case[j][i] = case[i][j]
             
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if new_case[i][j] == 1:
                cnt += 1
            else:
                ans += cnt
    
    print(ans)
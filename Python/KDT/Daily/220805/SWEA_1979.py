import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for tc in range(1, T + 1):
    # n: 배열 크기, k : 필요한 빈 칸 수
    n, k = map(int, input().split())

    case = [list(map(int, input().split())) for _ in range(n)]
    word = 0

    # 가로의 경우
    for i in range(n):
        cnt = 0
        for j in range(n):
            if case[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    word += 1
                cnt = 0
        if cnt == k:
            word += 1
        
    # 세로의 경우
    for i in range(n):
        cnt = 0
        for j in range(n):
            if case[j][i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    word += 1
                cnt = 0
                
        if cnt == k:
            word += 1


    print('#{} {}'.format(tc, word))
            

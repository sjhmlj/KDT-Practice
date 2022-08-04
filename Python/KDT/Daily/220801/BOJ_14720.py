'''
딸기 -> 초코 -> 바나나 -> 딸기 ...
우유가게 일렬 <- 시작부터 끝까지 걸으면서 우유 구매
각각의 가게는 하나만 취급
마실 수 있는 최대 개수
0 : 딸기
1 : 초코
2 : 바나나

'''

import sys

input = sys.stdin.readline

n = int(input())
case = list(map(int, input().split()))
cnt = 0


for i in range(len(case)):
    if case[i] == cnt % 3:
        cnt += 1

print(cnt)
        
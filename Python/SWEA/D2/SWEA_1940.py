'''
* 문제 : RC카 칸 이동 거리 계산
* 접근
    * 유지(0), 가속(1), 감속(2)
'''

import sys

sys.stdin = open('input_1940.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    n = int(input())
    total_speed = 0
    distance = 0

    for j in range(n):
        speed = list(map(int, input().split()))

        if speed[0] == 1:
            total_speed += speed[1]
        elif speed[0] == 2 and total_speed < speed[1]:
            total_speed = 0
        elif speed[0] == 2 and total_speed >= speed[1]:
            total_speed -= speed[1]
    
        distance += total_speed
    
    print('#{} {}'.format(i, distance))
'''
Q. 트럭 주차 비용 계산
한 대 주차 : 한 대 당 A원 / min
두 대 주차 : 한 대 당 B원 / min
세 대 주차 : 한 대 당 C원 / min
'''
import sys

sys.stdin = open('input_2979.txt', 'r')

A, B, C = map(int, input().split())
check = {}

for _ in range(3):
    time_in, time_out = map(int, input().split())
    
    for time in range(time_in, time_out):
        if time in check:
            check[time] += 1
        else:
            check[time] = 1

ans = 0

# {1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1}
for key in check:
    if check[key] >= 3:
        ans += check[key] * C
    elif check[key] >= 2:
        ans += check[key] * B
    elif check[key] >= 1:
        ans += check[key] * A

print(ans)

'''
절댓값 힙
1. 배열에 정수 x를 넣음
2. 배열에서 절댓값이 가장 작은 값 출력, 배열에서 제거
- 그 값이 여러개일 때는 원래 값이 가장 작은 수 출력, 제거
'''

import sys
import heapq

input = sys.stdin.readline

# 연산의 개수
n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

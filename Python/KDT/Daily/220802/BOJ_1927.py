import heapq
import sys

input = sys.stdin.readline

n = int(input())
list_ = []

heapq.heapify(list_)

for i in range(n):
    x = int(input())

    if x == 0 and len(list_) == 0:
        print(0)
    elif x == 0:
        print(heapq.heappop(list_))       
    else:
        heapq.heappush(list_, x)
    
  

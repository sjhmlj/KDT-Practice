'''
- 1~n까지 차례대로
- 한 장남을 때까지 반복
- 제일 위 카드를 버리고 그다음 위에있는 카드를 제일 아래로
- 
'''
from collections import deque

n = int(input())

queue = deque(range(1, n + 1))
waste = []

for i in range(len(queue)):
    if len(queue) == 1:
        break

    w = queue.popleft() 
    waste.append(w)
    queue.append(queue.popleft())

for i in waste:
    print(i, end=' ')

for i in queue:
    print(i, end=' ')
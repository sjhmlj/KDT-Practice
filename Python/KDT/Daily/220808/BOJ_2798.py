'''
Q. 블랙잭
- 카드 : 양의 정수
- n장의 카드를 숫자가 보이도록, m을 외침
- n장의 카드 중 3장의 카드를 골라야함
- 카드의 합 => m과 최대한 가까운 값을 만든다
'''

N, M = map(int, input().split())
case = list(map(int, input().split()))

max_ = 0
# 겹치지 않게 범위 설정해야겠음

# 3장의 카드 => 3중 for loop
for i in range(N - 2):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            val_ = case[i] + case[j] + case[k]
            if max_ < val_ <= M:
                max_ = val_

print(max_)
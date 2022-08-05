# deque 문제

from collections import deque
import sys

sys.stdin = open("_암호생성기.txt")

for _ in range(10):
    T = int(input())
    case = list(map(int, input().split()))
    target = deque(case)
    cnt = 1

    while True:
        x = target.popleft() - cnt

        # cycle 만족 => cnt 초기화
        if cnt == 5:
            cnt = 0

        # 0보다 작거나 같아지는 경우 알고리즘 동료
        if x <= 0:
            x = 0
            target.append(x)
            break

        target.append(x)
        cnt += 1

    print('#{}'.format(T),end=' ')
    for n in target:
        print(n, end=' ')
    print()
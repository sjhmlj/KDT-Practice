''''
본 숫자들 => 수첩 1
M개의 질문을 던짐
봤다고 대답한 숫자 => 수첩 2

수첩 2에 적혀있는 순서대로, 각각의 수에 대하여 있으면 1 없으면 0
'''

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())  # 수첩 1
    note1 = set(map(int, input().split()))

    m = int(input())  # 수첩 2
    note2 = list(map(int, input().split()))

    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)
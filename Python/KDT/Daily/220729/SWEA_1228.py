'''
* 문제 : 암호문 1
- 0 ~ 999,999 사이의 수를 나열하여 암호문
- 암호문 수정 프로그램을 작성

* output
수정된 결과의 처음 10개 숫자 출력
'''

import sys

sys.stdin = open('input_1228.txt', 'r')

for i in range(1, 10 + 1):
    n = int(input())
    origin = input().split()
    n_command = int(input())
    command = input().split()

    print('#{}'.format(i), end=' ')

    for j in range(len(command)):
        if command[j] == 'I':
            insert_idx = int(command[j + 1])
            insert_num = int(command[j + 2])
            
            for k in range(insert_num):
                origin.insert(insert_idx + k, command[j + 3 + k])

    for j in range(10):
        print(origin[j], end=' ')
    print()

'''
* 문제 : 직사각형 길이 찾기
네 변 중 세 변의 길이가 주어짐 => 한 쌍, 다른 하나

* input
1) test case T
2) 각 변의 길이 a, b, c (공백 구분)

* output
1) 나머지 변의 길이
'''

import sys

sys.stdin = open('input_3456.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    a, b, c = map(int, input().split())
    list_ = [a, b, c]
    for j in list_:
        if list_.count(j) == 1:
            result = j
            break
    else:
        result = a
    
    print('#{} {}'.format(i, result))

'''
* 문제 : 문자열의 거울상
주어진 문자열이 거울상을 가졌을 때의 모양 출력

* input
1) test case T
2) string case 

* output
1) case에 대한 거울상 출력

* algorithm
1) 뒤집고 치환 : bdppq -> qppdb -> pqqbd
'''

import sys

sys.stdin = open('input_10804.txt', 'r')

# input 1) test case
T = int(input())

# input 2) case
for i in range(1, T + 1):
    case = input()  # str

    mirror = case[::-1]  # 주어진 문자열을 뒤집음
    result = ''

    for word in mirror:
        if word == 'b': result += 'd'
        elif word == 'd': result += 'b'
        elif word == 'p': result += 'q'
        else: result += 'p'
    
    print('#{} {}'.format(i, result))

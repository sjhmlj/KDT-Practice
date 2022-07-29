'''
* 문제 : 신용카드 만들기1
- 신용카드는 룬 공식(마지막 열여섯번째 숫자 찾기)을 만족해야 함
1) 매 홀수자리의 숫자마다 2를 곱해서 더함
2) 매 짝수자리의 숫자는 그대로 더함
3) 1)과 2)를 더 한 숫자에 n을 더 한 숫자가 10으로 나눴을 때 나눠 떨어지면 만족
- 15개 번호가 주어졌을 때 마지막 N을 구하라

* input
1) test case T
2) card number (15자리)

* output
1) 룬 공식을 활용하여 16번째 번호 출력

* 참고
- idx 0번째 숫자 => 홀수
'''

import sys

sys.stdin = open('input_14649.txt', 'r')

# input 1) test case
T = int(input())

for i in range(1, T + 1):
    card_number = list(map(int, input().split()))
    sum_ = 0

    for j in range(len(card_number)):
        if (j+1) % 2 == 0:
            sum_ += card_number[j]
        else:
            sum_ += (card_number[j] * 2)
       
    for k in range(10):
        temp = sum_ + k

        if temp % 10 == 0:
            result = k
            break
    
    print('#{} {}'.format(i, result))


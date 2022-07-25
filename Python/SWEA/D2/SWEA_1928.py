'''
* 문제 : 특정 방식의 encoding 수행 (base64)
* 접근
    * 문자에 대응하는
    * 주어진 table에 따른 encoding list 작성
    * library 사용 X
'''

import sys

sys.stdin = open('input_1928.txt', 'r')

decode_table = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '0','1','2','3','4','5','6','7','8','9','+','/'
        ]

T = int(input())

for i in range(1, T + 1):
    case = input()
    text = ''

    for char in case:
        num = decode_table.index(char)
        temp_bin = bin(num)[2:]

        while len(temp_bin) < 6:
            temp_bin =  '0' + temp_bin
        text += temp_bin

        result = ''
        for j in range(0, len(text), 8):
         char = chr(int(text[j : j+8], 2))
         result += char
            
        
    print('#{} {}'.format(i, result))

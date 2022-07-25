'''
* I : test case T / 공백구분 하여 반복횟수 r, 문자열 s
* O : 조건에 따른 p출력
'''

T = int(input())

for i in range(1, T + 1):
    r, s = input().split()

    for c in s:
        print(c * int(r), end='')
    print()
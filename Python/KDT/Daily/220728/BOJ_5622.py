'''
* 다이얼 문제
* 1을 걸려면 총 2초, 한 칸씩 넘어갈수록 1초 더 걸림
'''
# 1, 0은 문자 맵핑 x
dial = {
    'ABC':'2',
    'DEF':'3',
    'GHI':'4',
    'JKL':'5',
    'MNO':'6',
    'PQRS':'7',
    'TUV':'8',
    'WXYZ':'9'
}
word = input()
number = ''

# 알고리즘1 : 입력 문자 -> 전화번호
for char in word:
    for dial_alphabet in dial:
        if char in dial_alphabet:
            number += dial[dial_alphabet]

# 알고리즘2 : 전화번호 누르는데에 걸리는 시간
call_time = 0

for digit in number:
    call_time += (int(digit) + 1)

print(call_time)
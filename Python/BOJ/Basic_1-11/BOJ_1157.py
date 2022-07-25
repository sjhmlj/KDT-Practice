'''
* 가장 많이 사용된 알파벳, 단 대소문자 구분 X
* I : 단어
* O : 여러개일 경우 '?' 출력
'''

word = input()

case = {}

for c in word:
    if c.upper() in case:
        case[c.upper()] += 1
    else:
        case[c.upper()] = 1

max_val = 0

for key in case:
    if max_val < case[key]:
        max_val = case[key]
        max_word = key
    elif max_val == case[key]:
        max_word = '?'

print(max_word)

        
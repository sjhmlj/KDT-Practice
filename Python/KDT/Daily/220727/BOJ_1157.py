'''
* I : 대소문자 단어
* O : 가장 많이 사용된 알파벳 (대소문자 구분 x)
    * 정답이 여러개일 경우 '?' 출력
'''
# 시간 초과 
word = input().upper()  # 대소문자 구분하지 않으니 대문자로 변환
max_count = 0

for char in word:
    char_cnt = word.count(char)
    if max_count < char_cnt:
        max_count = char_cnt
        max_alphabet = char
    elif max_count == char_cnt:
        max_alphabet = '?'

# print(max_alphabet)

# dict 활용 -- 통과
word = input().upper()

char_box = {}

for char in word:
    if char in char_box:
        char_box[char] += 1
    else:
        char_box[char] = 1

max_count = 0

for key in char_box:
    if max_count < char_box[key]:
        max_count = char_box[key]
        max_alphabet = key
    elif max_count == char_box[key]:
        max_alphabet = '?'

print(max_alphabet)
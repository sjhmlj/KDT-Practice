'''
* I : 단어 s, 알파벳 소문자로만 이루어짐
* O : 각각의 알파벳이 처음 등장하는 index (없을 경우 -1)
    * a : 0, b : 1, c : 2, ... z : 25 
'''

s = input()

# find() 활용
for i in range(ord('a'), ord('z') + 1):
    print(s.find(chr(i)), end = ' ')

# 직접 구현
check = ''
for i in range(ord('a'), ord('z') + 1):
    idx = -1
    for char in range(len(s)):
        if s[char] in check:
            continue
        elif chr(i) == s[char]:
            idx = char
            check += s[char]
    print(idx, end = ' ')


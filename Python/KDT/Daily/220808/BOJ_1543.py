'''
Q. 문서 검색
- 영어로만 이루어진 어떤 문서를 검색하는 함수를 만들고자함
- 중복되어 세는 것은 빼고 세야함
ex) 문서 : abababa / 서치 : ababa / 0번, 2번에서 찾을 수 있음 (동시에 X)
'''

text = input()
search = input()

cnt = 0
i = 0

while i <= len(text):
    if search == text[i : i + len(search)]:
        cnt += 1
        i += len(search)
    else:
        i += 1

print(cnt)

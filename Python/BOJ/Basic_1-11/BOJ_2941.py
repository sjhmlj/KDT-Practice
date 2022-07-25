'''
* 크로아티아 알파벳
* I : 알파벳 소문자, '-', '='
* O : 크로아티아 알파벳 숫자
    * 목록에 있는 알파벳 우선
    * 목록에 없으면 count 1
* 문제를 바라보는 시각을 창의적으로 가져가야함
'''

word = input()  # ddz=z= (3)
croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

# 처음 풀이 : 문자열에 대해 직관적으로 접근함
# 공백을 넣고 빼는 방식으로 문자열끼리 구분하여서 카운트
# 다소 비효율적이라고 느낌
for alphabet in croatia_list:
    if alphabet in word:
        cnt += word.count(alphabet)
        word = word.replace(alphabet, ' ')
    
word = word.replace(' ','')
print(cnt + len(word))


# 문제 자체를 효율적으로 접근
for alphabet in croatia_list:
    word = word.replace(alphabet, '*')

print(len(word))




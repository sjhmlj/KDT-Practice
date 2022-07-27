'''
'CAMBRIDGE'에 포함된 단어가 있다면 모두 삭제.
'''

text = input()

for word in 'CAMBRIDGE':
    text = text.replace(word, '')

print(text)
    

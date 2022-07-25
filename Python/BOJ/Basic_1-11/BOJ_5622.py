'''
* I : 대문자 단어 (2 <= len(word) <= 15)
* O : 다이얼을 걸기 위해 필요한 최소 시간
'''

# 반복문
word = input().upper()
dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for char in word:
    for i in range(len(dial_list)):
        if char in dial_list[i]:
            time += (i + 3)
print(time)

# for문 순서 바꾸기
time = 0
for i in range(len(dial_list)):
    for char in word:  # 'WA'
        if char in dial_list[i]:
            time += (i + 3)
print(time)


# 조건문으로 풀기
digit = ''

for i in range(len(word)):
    if ord(word[i]) in [65, 66, 67]:
        digit += '2'
    elif ord(word[i]) in [68, 69, 70]:
        digit += '3'
    elif ord(word[i]) in [71, 72, 73]:
        digit += '4'
    elif ord(word[i]) in [74, 75, 76]:
        digit += '5'
    elif ord(word[i]) in [77, 78, 79]:
        digit += '6'
    elif ord(word[i]) in [80, 81, 82, 83]:
        digit += '7'
    elif ord(word[i]) in [84, 85, 86]:
        digit += '8'
    elif ord(word[i]) in [87, 88, 89, 90]:
        digit += '9'

time = 0

for num in digit:
    time += int(num) + 1

print(time)
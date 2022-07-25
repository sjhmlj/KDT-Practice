'''
* I : 단어 개수 n / n개의 단어 (소문자, 중복 X, 최대 100)
* O : 그룹단어 갯수
* 공략 포인트
    * 오답의 경우로 접근
'''

n = int(input())
result = n  # 최댓값 == 단어 갯수, 미리 setting

for i in range(n):
    case = input()  # 단어 입력
    for j in range(len(case) - 1):
        if case[j] == case[j + 1]:
            pass
        elif case[j] in case[j + 1:]:
            result -= 1
            break

print(result)


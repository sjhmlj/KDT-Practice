croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


word = input()
cnt = 0
# 풀이 1) 문자열에 하나씩 접근
# replace() => 한 개씩 변경 X, 전부 다 변경. 
# 테스트 케이스 4번 : c=c= 의 경우 result = 1
# count method로 해결
for croa_alpha in croatia_list:
    if croa_alpha in word:
        cnt += word.count(croa_alpha)
        word = word.replace(croa_alpha, ' ')
        
result = len(word.replace(' ','')) + cnt
print(result)


# 풀이 2) 크로아티아 문자를 한 개로 치환하기
for croa_alpha in croatia_list:
    word = word.replace(croa_alpha, '*')

print(len(word))
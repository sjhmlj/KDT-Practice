'''
* 수 10개 입력
* 이를 42로 나눈 나머지 구함
* 서로 다른 값 몇 개 있는지 출력
'''
# 풀이 1 ) 자료구조 활용
num = []
for i in range(10):
    n = int(input()) % 42
    num.append(n)

print(len(set(num)))

# 풀이 2 ) 억지로지만 dict 활용
result = {}
for i in num:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1


print(len(result))

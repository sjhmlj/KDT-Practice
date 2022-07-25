'''
* 문제 : 주사위 3개의 눈의 같고 다름을 고려한 상금 계산
* 접근
    * 같은 눈 3개 / 같은 눈 2개 / 모두 다른 경우 분기
    * 같은 눈 2개의 경우 구분하여서 나눔
'''

a, b, c = map(int, input().split())

if a == b == c:
    result = 10000 + (a * 1000)
elif a == b or b == c:
    result = 1000 + (b * 100)
elif a == c:
    result = 1000 + (a * 100)
else:
    result = max(a, b, c) * 100

print(result)

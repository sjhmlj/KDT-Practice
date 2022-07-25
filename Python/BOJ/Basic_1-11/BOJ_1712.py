'''
* 손익분기점
* I : 고정 비용(a), 가변 비용(b), 소비자 가격(c)
* O : 손익분기점을 달성하는 순간의 판매량, 없으면 -1
* 수식에 대한 이해 및 활용까지 필요함!
'''

a, b, c = map(int, input().split())

if b >= c:
    result = -1
else:
    result = (a // (c - b)) + 1

print(result)
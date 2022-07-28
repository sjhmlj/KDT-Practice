'''
* 시간 복잡도 최소를 위해 .count() 방법 X
'''

n = int(input())
card = list(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))

case = {}

for i in card:
    if i in case:
        case[i] += 1
    else:
        case[i] = 1


for i in target:
    if i in case:
        print(case[i], end=' ')
    else:
        print(0, end=' ')
    
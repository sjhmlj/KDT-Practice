'''
* case
1) 1~8 차례대로 => ascending
2) 8~1 차례대로 => descending
3) 둘 다 아님 => mixed
'''

case = list(map(int, input().split()))

if case == sorted(case):
    result = 'ascending'
elif case == sorted(case, reverse=True):
    result = 'descending'
else:
    result = 'mixed'

print(result)

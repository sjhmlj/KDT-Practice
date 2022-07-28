'''
* 쉽게 푸는 문제
'''

problems = []

a, b = map(int, input().split())

for i in range(1, 1000 + 1):
    for _ in range(i):
        problems.append(i)

print(sum(problems[a-1:b]))
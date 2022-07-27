'''
키와 몸무게를 각각 비교하여 양쪽 모두 클 경우 <큰 덩치>
등수 = 나보다 큰 사람 수 + 1
같은 등수 여러명 허용
'''

n = int(input())  # 비교할 사람수

size = []

for i in range(n):
    person = list(map(int, input().split()))
    size.append(person)

# 2차원 배열로 접근
for i in range(len(size)):
    rank = 1
    for j in range(len(size)):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            rank += 1
    print(rank, end=' ')
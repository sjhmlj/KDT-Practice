'''
소의 위치 n번 관찰
소의 번호(1~10), 소의 위치(0 : 왼쪽 / 1: 오른쪽)로 기록

소가 최소 몇 번 길을 건너갔나?
'''
data = {}
for _ in range(int(input())):
    num, position = map(int, input().split())
    if num in data:
        if position != data[num][-1]:
            data[num].append(position)
    else:
        data[num] = [position]

cnt = 0
for key in data:
    cnt += len((data[key])) - 1

print(cnt)
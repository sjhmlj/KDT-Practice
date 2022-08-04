'''
n권을 m개의 더미로 쌓아둠 -> stack?
교과서 정리하여 번호순 나열
교과서 : 1~n 라벨링
맨 위에 있는 교과서만 꺼낼 수 있음 -> stack!
꺼낸 순서대로 나열

* stack (LIFO) 문제 -> push, pop
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

box = []

for i in range(m):
    idx = int(input())
    case = list(map(int, input().split()))
    box.append(case)

for i in range(len(box)):
    if box[i] != sorted(box[i], reverse=True):
        print("No")
        break
else:
    print("Yes")
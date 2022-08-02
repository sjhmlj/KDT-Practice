'''
자연수를 원소로 갖는 집합 A, B (공집합 x)
대칭차집합 출력
'''

import sys

input = sys.stdin.readline
# 두 집합 원소의 개수
a, b = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = (A-B) | (B-A)
print(len(result))
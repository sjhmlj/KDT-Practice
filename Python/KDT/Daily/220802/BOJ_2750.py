import sys

input = sys.stdin.readline

n = int(input())
case = []

for _ in range(n):
    case.append(int(input()))

for num in sorted(case):
    print(num)
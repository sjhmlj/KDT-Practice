import sys

lines = sys.stdin.read().replace(' ', '').replace('\n', '')


basket = {}

for char in lines:
    if char in basket:
        basket[char] += 1
    else:
        basket[char] = 1

result = sorted(basket.items(), key = lambda x : (-x[1], x[0]))
max_ = max(basket.values())

for char, cnt in result:
    if cnt == max_:
        print(char, end='')

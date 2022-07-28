N = int(input())  # 카드 개수
card = {}

for i in range(N):
    num = int(input())
    if num in card:
        card[num] += 1
    else:
        card[num] = 1 

result = sorted(card.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])
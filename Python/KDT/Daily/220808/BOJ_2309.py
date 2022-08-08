'''
Q. 일곱 난쟁이
- 난쟁이 : 7 -> 9
- 난쟁이 키의 합 : 100
'''

case = [int(input()) for _ in range(9)]
total = sum(case)
target = total - 100  # 뺄셈을 활용하지 않으면 브루트 포스 case (7중 for loop)

for i in range(9):
    for j in range(i + 1, 9):
        if target == case[i] + case[j]:
            x1 = case[i]
            x2 = case[j]
            case.remove(x1)
            case.remove(x2)
            break
    if len(case) == 7:
        break

for i in sorted(case):
    print(i)
